$(window).on('load', function() {
    frappe.after_ajax(function () {
        $(`<div class="novaBrandingClass"><p class="novaBrandingText">Powered by</p> <a class="novaBrandingAttribute" href="https://novacept.io/" target="_blank"><img class="novaBrandingImage" src="https://i.postimg.cc/R6BfWV4N/oie-j-PCa-Sj-Vh-QRAE.png" alt="logo" width="80"></a></div>`).insertAfter("#navbar-breadcrumbs") 
    })
})
