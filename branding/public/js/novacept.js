$(window).on('load', function() {
    frappe.after_ajax(function () {   
        if (frappe.boot.color_branding.navbar_background_color) {
            $('.navbar').css('background-color',frappe.boot.color_branding.navbar_background_color)
        } 
        if (frappe.boot.color_branding.container_bg_color) {
            $('.page-container').css('background',frappe.boot.color_branding.container_bg_color)
        }
        $(`<div class="novaBrandingClass"><p class="novaBrandingText">Powered by</p> <a class="novaBrandingAttribute" href="https://novacept.io/" target="_blank"><img class="novaBrandingImage" src="https://i.postimg.cc/xXsCgdFB/color-Logo-Novacept.png" alt="logo" width="80"></a></div>`).insertAfter("#navbar-breadcrumbs")   
    })
})
