import unittest
from EmailExtractor import EmailExtractor

class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            # email, student, is_female, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, False, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, False, "Jan", "Kowalski"],
            ["anna.nowak03@student.wat.edu.pl", True, True, "Anna", "Nowak"],
            ["adrianna.abacka@student.wat.edu.pl", True, True, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, True, "Katarzyna", "Babacka"],
            ["agnieszka.zalewska01@student.wat.edu.pl", True, True, "Agnieszka", "Zalewska"],
            ["michal.jarosz@wat.edu.pl", False, False, "Michal", "Jarosz"],
            ["lukasz.laszko@wat.edu.pl", False, False, "Lukasz", "Laszko"],
            ["lukasz.skibniewski@wat.edu.pl", False, False, "Lukasz", "Skibniewski"],
            ["witold.zorski@wat.edu.pl", False, False, "Witold", "Zorski"],
            ["michal.brzozowski03@student.wat.edu.pl", True, False, "Michal", "Brzozowski"],
            ["mateusz.stolarski@student.wat.edu.pl", True, False, "Mateusz", "Stolarski"],
            ["bartosz.betanski@student.wat.edu.pl", True, False, "Bartosz", "Betanski"],
            ["jan.nowowiejski@student.wat.edu.pl", True, False, "Jan", "Nowowiejski"],
            ["izabela.borkowska01@student.wat.edu.pl", True, True, "Izabela", "Borkowska"],
            ["aleksandra.puzon05@student.wat.edu.pl", True, True, "Aleksandra", "Puzon"],
            ["marcin.laskowski01@student.wat.edu.pl", True, False, "Marcin", "Laskowski"],
            ["radoslaw.wozniak@wat.edu.pl", False, False, "Radoslaw", "Wozniak"]
        ]

    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_student = x[1]
                # then
                extractor = EmailExtractor(email)
                extractor.parse()
                # expect
                self.assertEqual(is_student, extractor.is_student())

    def test_is_female(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_female = x[2]
                # then
                extractor = EmailExtractor(email)
                extractor.parse()
                # expect
                self.assertEqual(is_female, extractor.is_female())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                extractor.parse()
                # expect
                self.assertEqual(surname, extractor.get_surname())



    def test_get_name(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                extractor.parse()
                # expect
                self.assertEqual(name, extractor.get_name())