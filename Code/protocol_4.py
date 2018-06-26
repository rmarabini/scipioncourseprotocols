# place this code in the directory
# $SCIPION_HOME/pyworkflow/em/packages/xmipp3
# edit the file
# $SCIPION_HOME/pyworkflow/em/packages/__init__.py
# and add the line
# from protocol_1 import XmippProtABS
# launch scipion
# create project and search for new protocol
# CTRL-F

# STEP-1: see GUI
# STEP 1.5: test GUI
# STEP 1.6: validator=[NonEmpty]
# STEP-2: add runOperateStep
# STEP 3: add convertStep -> convert input to mrc if needed
# STEP 4: add createOutputStep -> set of XXXXX
# STEP 5: add validation -> check xmipp_operate exists
# STEP 6: add citation// methods
# STEP 7: USE as input tow sets of images and add them

from pyworkflow.em.protocol import EMProtocol
from pyworkflow.protocol.params import PointerParam, IntParam
from pyworkflow.em.packages.xmipp3.convert import (writeSetOfParticles)
from pyworkflow.object import String
import pyworkflow.em.metadata as md
from convert import writeSetOfParticles, xmippToLocation

class XmippProtABS(EMProtocol):
    """
    compute the absolute value of a set of images
    """
    _label = 'abs'

    def __init__(self, **kwargs):
        EMProtocol.__init__(self, **kwargs)

    #--------------- DEFINE param functions ---------------

    def _defineParams(self, form):
        form.addSection(label='Params')
        group = form.addGroup('Input')
        group.addParam('inputParticles',
                       PointerParam,
                       pointerClass='SetOfParticles',
                       label="Input images",
                       help='Images to be processed')

    #--------------- INSERT steps functions ----------------

    def _insertAllSteps(self):
        self._defineFilenames()
        self._insertFunctionStep('convertInputStep')
        self._insertFunctionStep('runOperateStep')
        self._insertFunctionStep('createOutputStep')

    #--------------- STEPS functions -----------------------

    def convertInputStep(self):
        writeSetOfParticles(self.inputParticles.get(), self.inputFn)

    def runOperateStep(self):
        # metadata outmetadata.xmd
        args = "-i %s --abs -o %s" % (self.inputFn, self.outputStk)
        self.runJob("xmipp_image_operate", args)

    def createOutputStep(self):
        inputSet = self.inputParticles.get()
        outputSet = self._createSetOfParticles()
        outputSet.copyInfo(inputSet)
        outputSet.copyItems(inputSet,
                        updateItemCallback=self._updateItem,
                        itemDataIterator=md.iterRows(
                                self.outputMd,
                                sortByLabel=md.MDL_ITEM_ID)
                            )
        self._defineOutputs(outputSet=outputSet)
    #--------------- INFO functions -------------------------

    def _validate(self):
        return []

    def _citations(self):
        cites = ['delaRosaTrevin2013']
        return cites

    def _summary(self):
        message= "Processed %d images" % \
                 self.inputParticles.get().getSize()
        return [message]

    def _methods(self):
        return ["describe your method"]

    #--------------- UTILS functions -------------------------

    def _defineFilenames(self):
        self.inputFn = self._getTmpPath('input_particles.xmd')
        self.outputMd = self._getExtraPath('output_images.xmd')
        self.outputStk = self._getExtraPath('output_images.stk')

    def _updateItem(self, item, row):
        """ Implement this function to do some
        update actions over each single item
        that will be stored in the output Set.
        """
        # By default update the item location (index, filename)
        # with the new binary data location (after preprocessing)
        newFn = row.getValue(md.MDL_IMAGE)
        newLoc = xmippToLocation(newFn)
        item.setLocation(newLoc)
