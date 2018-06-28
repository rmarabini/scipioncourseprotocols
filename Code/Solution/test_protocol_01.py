"""
Basic template for a protocol test using particles as input.
"""

from pyworkflow.tests import BaseTest, setupTestProject, DataSet
from pyworkflow.em.protocol import ProtImportParticles
from pyworkflow.em.packages.xmipp3 import XmippProtABS, XmippProtPreprocessParticles


class TestXmippABS(BaseTest):
    @classmethod
    def setUpClass(cls):
        setupTestProject(cls)
        cls.ds = DataSet.getDataSet('relion_tutorial')
        inputStar = cls.ds.getFile('import/classify3d/extra/'
                                   'relion_it015_data.star')
        cls.protImport = cls.newProtocol(ProtImportParticles,
                                         objLabel='particles from relion (auto-refine 3d)',
                                        importFrom=ProtImportParticles.IMPORT_FROM_RELION,
                                        starFile=inputStar,
                                        magnification=10000,
                                        samplingRate=7.08,
                                        haveDataBeenPhaseFlipped=True)
        cls.launchProtocol(cls.protImport)

    def test1(self):
        protPreprocess = self.newProtocol(XmippProtPreprocessParticles,
                                          objLabel='invert contrast',
                                          doInvert=True)

        inputParts = self.protImport.outputParticles.get()
        protPreprocess.inputParticles.set(inputParts)

        self.launchProtocol(protPreprocess)

        outputParts = getattr(protPreprocess, 'outputParticles', None)

        self.assertNotNone(outputParts)
        self.assertEqual(outputParts.getSize(), inputParts.getSize())


    def test2(self):
        pass