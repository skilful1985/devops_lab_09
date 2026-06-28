#./server/test_application.py

import pytest					# используем библиотеку PyTest

from application import TestMe		# импортируем наше приложение

def test_server():
  assert TestMe().take_five() == 5		# проверка функции

def test_port():
  assert TestMe().port() == 8000 		# проверка другой функции