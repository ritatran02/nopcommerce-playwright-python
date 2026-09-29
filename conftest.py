import pytest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


@pytest.fixture
def page(context, request):
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    yield page

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        context.tracing.stop(
            path=PROJECT_ROOT / "test-results" / f"{request.node.name}-trace.zip"
        )
    else:
        context.tracing.stop()


@pytest.fixture
def authenticated_page(browser):
    context = browser.new_context(
        storage_state=PROJECT_ROOT / "auth" / "user.json"
    )

    page = context.new_page()

    yield page

    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, f"rep_{rep.when}", rep)