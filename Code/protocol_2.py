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
#################
# Add runOperateStep
#################

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

    #--------------- STEPS functions -----------------------
    
    def convertInputStep(self):
        writeSetOfParticles(self.inputParticles.get(), self.inputFn)

    def runOperateStep(self):
        args = "-i %s --abs -o %s" % (self.inputFn, self.outputStk)
        self.runJob("xmipp_image_operate", args)

#    def createOutputStep(self):
#        pass

    #--------------- INFO functions -------------------------

    def _validate(self):
        return []

#    def _citations(self):
#        return []

    def _summary(self):
        return []

#    def _methods(self):
#        return []

    #--------------- UTILS functions -------------------------

    def _defineFilenames(self):
        self.inputFn = self._getTmpPath('input_particles.xmd')
        self.outputMd = self._getExtraPath('output_images.xmd')
        self.outputStk = self._getExtraPath('output_images.stk')


