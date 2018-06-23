# place this code in the directory
# $SCIPION_HOME/pyworkflow/em/packages/xmipp3
# edit the file
# $SCIPION_HOME/pyworkflow/em/packages/__init__.py
# and add the line
# from protocol_1 import XmippProtABS
# launch scipion
# create project and search for new protocol
# CTRL-F


from pyworkflow.em.protocol import EMProtocol
from pyworkflow.protocol.params import PointerParam

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
        group.addParam('name_of_the_variable_that_stores_the_images',
                       PointerParam,
                       pointerClass='SetOfImages',
                       label="this appears in the GUI",
                       help='help message')

        # add a IntParam, if you do not konw how just search
        # for examples in $SCIPION_HOME/pyworkflow/em/packages/xmipp3

    #--------------- INSERT steps functions ----------------

    def _insertAllSteps(self):
        self._insertFunctionStep('runOperateStep')

    #--------------- STEPS functions -----------------------

#    def convertInputStep(self):
#        pass

    def runOperateStep(self, params):
        pass

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


