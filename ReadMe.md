Три тестовых задания.  
Задания выполнялись на языке Python, на компьютере с ОС Windows 7  
1. Задача "Копирование файла".  
"Реализовать программу, осуществляющую копирование файлов в соответствии с конфигурационным файлом.  
Конфигурационный файл должен иметь формат xml. Для каждого файла в конфигурационном файле должно быть указано его имя,  
исходный путь и путь, по которому файл требуется скопировать."  

Файлы:  
- first.py - файл с кодом решениея
- config.xml - файл с исходными данными


2. Задача "Проверка хэш-суммы".  
"Дан файл, содержащий имена файлов, алгоритм хэширования (один из MD5/SHA1/SHA256) и соответствующие им хэш-суммы, 
вычисленные по соответствующему алгоритму и указанные в файле через пробел. Напишите программу, читающую данный файл
и проверяющую целостность файлов."

Файлы:
- second.py -файл с кодом решения
- input_file.txt - файл с исходными данными
- file_04.txt - один из проверяемых фалов

3. Задача "Тестовая система".  
"Напишите прототип тестовой системы, состоящей из двух тест-кейсов. В данной задаче использование стороннего модуля 
для автоматизации тестирования не приветствуется.
Тестовая система представляет собой иерархию классов, описывающую тест-кейсы.  
У каждого тест-кейса есть:  
•	Номер (tc_id) и название (name)  
•	Методы для подготовки (prep), выполнения (run) и завершения (clean_up) тестов.  
•	Метод execute, который задаёт общий порядок выполнения тест-кейса и обрабатывает исключительные ситуации.  
Все этапы выполнения тест-кейса, а также исключительные ситуации должны быть задокументированы в лог-файле или в стандартном выводе."  

Файлы:
- third.py - файл с кодом решения
