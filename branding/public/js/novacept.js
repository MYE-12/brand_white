$(window).on('load', function() {
    frappe.after_ajax(function () {
        $(`<div class="novaBrandingClass"><p class="novaBrandingText">Powered by</p> <a class="novaBrandingAttribute" href="https://novacept.io/" target="_blank"><img class="novaBrandingImage" src="https://i.postimg.cc/xXsCgdFB/color-Logo-Novacept.png" alt="logo" width="80"></a></div>`).insertAfter("#navbar-breadcrumbs") 
    })
})
