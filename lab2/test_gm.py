from grades_management import  add_child, add_child_subjects, add_child_grades
import unittest



class TestOrderStack(unittest.TestCase):

    def setUp(self):
        self.data_dict = {}
        
    def test_add_child1(self):
        # Перевірка додавання першого учня
        child = ('8-A', 'Soroka I.I.')
        self.assertEqual(add_child(self.data_dict, child), 1) 

    def test_add_duplicate_child(self):
        # Перевірка спроби додати того ж самого учня
        child = ('8-A', 'Soroka I.I.')
        add_child(self.data_dict, child) 
        with self.assertRaises(ValueError):
            add_child(self.data_dict, child) 
        

    def test_add_children2(self):
        # Перевірка додавання декількох учнів
        child1 = ('8-A', 'Soroka I.I.')
        child2 = ('7-B', 'Kozak A.S.')
        self.assertEqual(add_child(self.data_dict, child1), 1) 
        self.assertEqual(add_child(self.data_dict, child2), 2)

    def test_add_subjects_to_existing_child(self):
            # Перевірка додавання предметів існуючому учню
        child = ('8-A', 'Soroka I.I.')
        subjects = ['Math', 'Ukr literature', 'Chemistry']
        add_child(self.data_dict, child)
        self.assertEqual(add_child_subjects(self.data_dict, child, subjects), 3)  # Очікуємо, що кількість предметів буде 3

    def test_add_subjects_to_non_existing_child(self):
        # Перевірка спроби додати предмети неіснуючому учню
        child = ('8-A', 'Soroka I.I.')
        subjects = ['Math', 'Ukr literature', 'Chemistry']
        with self.assertRaises(ValueError):
            add_child_subjects(self.data_dict, child, subjects)  # Спроба додати предмети неіснуючому учню має призвести до помилки

    def test_add_duplicate_subjects(self):
        # Перевірка спроби додати ті ж самі предмети
        child = ('8-A', 'Soroka I.I.')
        subjects = ['Math', 'Ukr literature', 'Chemistry']
        add_child(self.data_dict, child)  
        add_child_subjects(self.data_dict, child, subjects)
        with self.assertRaises(ValueError):
            add_child_subjects(self.data_dict, child, subjects)  # Спроба додати ті ж самі предмети має призвести до помилки

    def test_add_grades_to_existing_subject(self):
        # Перевірка додавання оцінок до існуючого предмету
        child = ('8-A', 'Soroka I.I.')
        subject = 'Math'
        grades_list = [12, 10, 8, 9]
        add_child(self.data_dict, child) 
        add_child_subjects(self.data_dict, child, [subject]) 
        self.assertEqual(add_child_grades(self.data_dict, child, subject, grades_list), 4)  # Очікуємо, що кількість оцінок буде 4

    def test_add_grades_to_non_existing_subject(self):
        # Перевірка додавання оцінок до неіснуючого предмету
        child = ('8-A', 'Soroka I.I.')
        subject = 'Math'
        grades_list = [12, 10, 8, 9]
        add_child(self.data_dict, child)
        with self.assertRaises(ValueError):
            add_child_grades(self.data_dict, child, subject, grades_list)  # Спроба додати оцінки до неіснуючого предмету має призвести до помилки

    def test_add_grades_to_non_existing_child(self):
        # Перевірка спроби додати оцінки неіснуючому учню
        child = ('8-A', 'Soroka I.I.')
        subject = 'Math'
        grades_list = [12, 10, 8, 9]
        with self.assertRaises(ValueError):
            add_child_grades(self.data_dict, child, subject, grades_list)  # Спроба додати оцінки неіснуючому учню має призвести до помилки

if __name__ == "__main__":
    unittest.main()
