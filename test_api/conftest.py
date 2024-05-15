from datetime import datetime
import pytest
from settings import BASE_URL
import pytest_html


@pytest.fixture(autouse=True)
def time_delta():
    """
    Calculate and print test execution time
    """
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(f"\nТест прошёл за: {end_time - start_time}")


def pytest_addoption(parser):
    parser.addoption("--testurl", action="store", default=BASE_URL)


@pytest.fixture(scope='session')
def testurl(request):
    """Return new 'testurl' value  taken from the extension of pytest
    command line: "--testurl" "new_test_url" (optional)
    If not indicated, the default value is provided"""
    testurl_value = request.config.option.testurl
    if testurl_value is None:
        pytest.skip()
    return testurl_value


def get_test_case_docstring(item):
    """ This function gets doc string from test case and format it
        to show this docstring instead of the test case name in reports.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ This function modifies names of test cases "on the fly"
        during the execution of test cases.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ This function modified names of test cases "on the fly"
        when we are using --collect-only parameter for pytest
        (to get the full list of all existing test cases).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to
            # it's doc string to show human-readable reports and to
            # automatically import test cases to test management system.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()


@pytest.fixture(scope="session", autouse=True)
def failure_tracking_fixture(request):
    tests_failed_before_module = request.session.testsfailed
    yield
    tests_failed_during_module = request.session.testsfailed - tests_failed_before_module
    if tests_failed_before_module or tests_failed_during_module:
        import time
        current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
        text_to_send = f"Pytest results {current_time}"
        # send_email_attachment(text_to_send, 'report.html')
        # print("e-mail report sent")
        print(text_to_send)
