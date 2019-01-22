var sidebarSwitchBtnEl = $('#sidebar-switch-btn');
var sidebarEl = $("sidebar");

sidebarSwitchBtnEl.on('click', function(){
    sidebarEl.toggleClass('show'); 
});