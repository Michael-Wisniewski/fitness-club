var headerEl = $('#header-top')
var headerLoginButtonEl = headerEl.find('#login-container button');
var headerMenuEl = headerEl.find('#navbar-container .navbar-collapse');

headerLoginButtonEl.on('click', function() {
    headerMenuEl.removeClass('show');
});