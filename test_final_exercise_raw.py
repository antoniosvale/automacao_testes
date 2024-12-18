# Generated by Selenium IDE
import pytest
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:
    """Classe que encapsula as interações com a página inicial do site."""

    def __init__(self, driver):
        """
        Inicializa a instância da página inicial.

        Args:
            driver (webdriver): Instância do navegador controlada pelo Selenium.
        """
        self._driver = driver

    def on_page_load(self):
        """
        Aguarda o carregamento completo da página, verificando a presença de elementos
        identificados pelo seletor CSS '.smooth' e aguardando até que sejam removidos.
        """
        elements = self._driver.find_elements(By.CSS_SELECTOR, ".smooth")
        while len(elements) > 0:
            elements = self._driver.find_elements(By.CSS_SELECTOR, ".smooth")
            time.sleep(0.2)

    def new_discipline(self, discipline):
        """
        Cadastra uma nova disciplina no sistema.

        Args:
            discipline (str): Nome da disciplina a ser criada.
        """
        self._driver.find_element(By.ID, "discipline-nome").click()
        self._driver.find_element(By.ID, "discipline-nome").clear()
        self._driver.find_element(By.ID, "discipline-nome").send_keys(discipline)
        self._driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn"
        ).click()

    def add_student_discipline(self, student_id, discipline_id):
        """
        Inscreve um estudante em uma disciplina.

        Args:
            student_id (str): ID do aluno.
            discipline_id (str): ID da disciplina.
        """
        self._driver.find_element(By.ID, "subscribe-student-id").click()
        self._driver.find_element(By.ID, "subscribe-student-id").clear()
        self._driver.find_element(By.ID, "subscribe-student-id").send_keys(student_id)
        self._driver.find_element(By.ID, "subscribe-discipline-id").click()
        self._driver.find_element(By.ID, "subscribe-discipline-id").send_keys(
            discipline_id
        )
        self._driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn"
        ).click()

    def new_course(self, course):
        """
        Cadastra um novo curso no sistema.

        Args:
            course (str): Nome do curso a ser criado.
        """
        self._driver.find_element(By.ID, "course-nome").click()
        element = self._driver.find_element(By.ID, "course-nome")
        actions = ActionChains(self._driver)
        actions.double_click(element).perform()
        self._driver.find_element(By.ID, "course-nome").send_keys(course)
        self._driver.find_element(By.ID, "course-btn").click()

    def add_discipline_course(self):
        """
        Relaciona uma disciplina a um curso, associando-os no sistema.
        """
        self._driver.find_element(By.ID, "discipline-nome").click()
        self._driver.find_element(By.ID, "discipline-nome").send_keys("mat")
        self._driver.find_element(By.ID, "course-discipline-id").click()
        self._driver.find_element(By.ID, "course-discipline-id").send_keys("1")
        self._driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn"
        ).click()

    def add_student_course(self):
        """
        Inscreve um aluno em um curso.
        """
        self._driver.find_element(By.ID, "student-id").click()
        self._driver.find_element(By.ID, "student-id").send_keys("1")
        self._driver.find_element(By.ID, "course-id").click()
        self._driver.find_element(By.ID, "course-id").send_keys("1")
        self._driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(4) > #course-btn"
        ).click()

    def new_student(self, student):
        """
        Cadastra um novo aluno no sistema.

        Args:
            student (str): Nome do aluno a ser criado.
        """
        self._driver.find_element(By.ID, "student-nome").click()
        self._driver.find_element(By.ID, "student-nome").send_keys(student)
        self._driver.find_element(By.ID, "student-btn").click()

    def get_message(self, index=1):
        """
        Obtém o texto de uma mensagem exibida na página.

        Args:
            index (int): Índice da mensagem a ser recuperada (1 para o primeiro elemento).
                         O padrão é 1.

        Returns:
            str: Texto da mensagem localizada.
        """
        return self._driver.find_element(
            By.CSS_SELECTOR, f".py-p:nth-child({index})"
        ).text


class TestDemo:
    """Classe de testes automatizados para o site."""

    def setup_method(self, method):
        """
        Configura o ambiente de teste, inicializando o navegador.

        Args:
            method: Método de teste atual (usado internamente pelo pytest).
        """
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        """
        Encerra o ambiente de teste, fechando o navegador.

        Args:
            method: Método de teste atual (usado internamente pelo pytest).
        """
        self.driver.quit()

    def test_demo(self):
        """
        Executa o fluxo de teste para criar e relacionar entidades no sistema,
        como estudantes, cursos e disciplinas, validando mensagens de retorno.
        """
        self.driver.get("https://tdd-detroid.onrender.com/")
        self.driver.set_window_size(970, 555)

        home_page = HomePage(self.driver)
        home_page.on_page_load()

        home_page.new_student(student="douglas")
        assert "INFO Added student id: 1, Name: douglas" in home_page.get_message()

        home_page.new_course(course="mat")
        assert "INFO Added student id: 1, Name: douglas" in home_page.get_message(2)

        home_page.add_student_course()
        assert "INFO Added student id: 1, Name: douglas" in home_page.get_message(3)

        home_page.add_discipline_course()
        assert (
            "FAIL Necessários 3 cursos para se criar a primeira matéria"
            in home_page.get_message()
        )

        home_page.new_course(course="port")
        home_page.new_course(course="geo")

        self.driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn"
        ).click()
        assert (
            "INFO Added discipline id: 1, Name: mat, Course: 1"
            in home_page.get_message()
        )

        home_page.new_discipline(discipline="mat2")
        home_page.new_discipline(discipline="mat3")

        home_page.add_student_discipline(student_id="1", discipline_id="1")
        assert (
            "WARN Aluno deve se inscrever em 3 materias no minimo"
            in home_page.get_message()
        )

        home_page.add_student_discipline(student_id="1", discipline_id="2")
        home_page.add_student_discipline(student_id="1", discipline_id="3")

        home_page.new_discipline(discipline="mat4")

        home_page.add_student_discipline(student_id="1", discipline_id="4")

        self.driver.close()
