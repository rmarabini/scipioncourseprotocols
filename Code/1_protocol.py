# place this code in the directory
# $SCIPION_HOME/pyworkflow/em/packages
from pyworkflow.em.protocol import EMProtocol
from pyworkflow.protocol.params import PointerParam

class XmippProtABS(EMProtocol):
    """
    compute the absolute value of a set of images
    """
    _label = 'abs'

    def __init__(self, **kwargs):
        pass

    #--------------- DEFINE param functions ---------------

    def _defineParams(self, form):
        form.addSection(label='Params')
        group = form.addGroup('Input')
        group.addParam('name_of_the_variable_that_stores_the_images',
                       PointerParam,
                       pointerClass='SetOfImages',
                       label="this appears in the GUI",
                       help='help message')
        pass

    #--------------- INSERT steps functions ----------------

    def _insertAllSteps(self):
        pass

    #--------------- STEPS functions -----------------------

    def convertInputStep(self):
        pass

    def runMLStep(self, params):
        pass

    def createOutputStep(self):
        pass

    #--------------- INFO functions -------------------------

    def _validate(self):
        return []

    def _citations(self):
        return []

    def _summary(self):
        return []

    def _methods(self):
        return []

    #--------------- UTILS functions -------------------------


