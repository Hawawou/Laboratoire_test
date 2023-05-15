import unittest
import HtmlTestRunner

# import test modules
import test_Agence
import test_addEmployee
import test_Famille
import test_Bonexamen
import test_Factures
import test_ModifFamille
import test_TypeExamens
import test_viewPatient
import test_Unite
import test_companie
import test_institution
import test_Examen

# initialize test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests
suite.addTests(loader.loadTestsFromModule(test_addEmployee))
suite.addTests(loader.loadTestsFromModule(test_Famille))
suite.addTests(loader.loadTestsFromModule(test_Bonexamen))
suite.addTests(loader.loadTestsFromModule(test_Factures))
suite.addTests(loader.loadTestsFromModule(test_ModifFamille))
suite.addTests(loader.loadTestsFromModule(test_TypeExamens))
suite.addTests(loader.loadTestsFromModule(test_viewPatient))
suite.addTests(loader.loadTestsFromModule(test_Unite))
suite.addTests(loader.loadTestsFromModule(test_companie))
suite.addTests(loader.loadTestsFromModule(test_institution))
suite.addTests(loader.loadTestsFromModule(test_Examen))


# initialize runner
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
reports = HtmlTestRunner.HTMLTestRunner(combine_reports=True,
                                        report_name="MyReport",
                                        add_timestamp="False").run(suite)
