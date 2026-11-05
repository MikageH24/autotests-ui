import pytest
import allure
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.severity(Severity.NORMAL)
    @allure.title("Check displaying of empty courses list")
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.severity(Severity.CRITICAL)
    @allure.title("Create course")
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0"
        )
        create_course_page.create_course_exercise_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image(file="./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10")
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )

    @allure.severity(Severity.CRITICAL)
    @allure.title("Edit course")
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.image_upload_widget.upload_preview_image(file="./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10")
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10"
        )
        courses_list_page.menu.click_edit()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright 2.0",
            estimated_time="3 weeks",
            description="Playwright 2.0",
            max_score="120",
            min_score="20"
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright 2.0",
            estimated_time="3 weeks",
            max_score="120",
            min_score="20"
        )
