from Teste.testCardClient import testCardClient
from Teste.testFunctionalitati import testFunctionalitatiMed
from Teste.testGenerator import testGenerator
from Teste.testMedicament import testMedicament
from Teste.testTranzactie import testTranzactie


def testAll():
    testCardClient()
    testMedicament()
    testTranzactie()
    testFunctionalitatiMed()
    testGenerator()
