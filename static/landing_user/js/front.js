$(function () {

    // ================================================
    //  NAVBAR BEHAVIOR
    // ================================================
    $(window).on('scroll load', function () {
        if ($(window).scrollTop() > 5) {
            $('.navbar').addClass('active');
        } else {
            $('.navbar').removeClass('active');
        }

        if ($(window).scrollTop() > 1000) {
            $('#scrollTop').addClass('active');
        } else {
            $('#scrollTop').removeClass('active');
        }
    });

    $.get( "/api/v1/categories/", function( data ) {
                        
        if(data.success){
            var data = data.data;
            $("#container_categories").empty();
            $.each(data, function( key, value ) {
                $("#container_categories").append(
                    '<div class="col-lg-3 col-sm-4 col-6 mb-4">'+
                    '<div class="card border-0 shadow rounded-lg text-left px-2">'+
                        '<div class="card-body px">'+
                            '<div class="row">'+
                                '<div class="col-lg-3 col-sm-2 col-12 mx-auto">'+
                                    '<img src="'+ value.image +'" width="30">'+ 
                                '</div>'+  
                                '<div class="col-lg-9 col-sm-10 col-12 mx-auto">'+
                                    '<p class="h6 text-muted">'+ value.name +'</p>'+   
                                '</div>'+ 
                            '</div>'+                        
                        '</div>'+
                    '</div>'+
                    '</div>');
            });
        }
    });    


    // ================================================
    //  TESTIMONIALS SLIDER
    // ================================================

    $.get( "/api/v1/markets/news/", function( data ) {                        
        if(data.success){
            var data = data.data;
            $("#container_markets").empty();
            $.each(data, function( key, value ) {
                $("#container_markets").append(
                    '<div class="mx-3 mx-lg-4 my-3 pt-3">'+
                    '<div class="card shadow rounded-lg px-3 py-4 px-lg-2 with-pattern bg-white border-0">'+
                        '<div class="card-body index-forward pt-5 rounded-lg">'+
                            '<h3>'+ value.name +'</h3>'+
                            '<p class="lead text-muted mb-5">'+ value.addresses +'</p>'+
                            '<h5 class="font-weight-bold mb-0">'+ value.city +'</h5>'+
                            '<p class="text-primary mb-0 text-small">'+ value.categories[0].name +'</p>'+
                        '</div>'+
                    '</div>'+
                    '</div>');
            });
        }

        $('.testimonials-slider').owlCarousel({
            items: 1,
            dots: true
        });
    });

    

    // ================================================
    //  MODAL VIDEO
    // ================================================
    //new ModalVideo('.js-modal-btn');


    // ================================================
    // Move to the top of the page
    // ================================================
    $('#scrollTop').on('click', function (e) {
        e.preventDefault();
        $('html, body').animate({ scrollTop: 0}, 1000);
    });

    // ================================================
    // Preventing URL update on navigation link click
    // ================================================
    $('.link-scroll').on('click', function (e) {
        var anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $(anchor.attr('href')).offset().top
        }, 1000);
        e.preventDefault();
    });


    // ================================================
    // Scroll Spy
    // ================================================
    $('body').scrollspy({
        target: '#navbarSupportedContent',
        offset: 80
    });
});
