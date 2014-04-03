$(document).ready(function(){
    //init class on right column

    if(!$('body').hasClass('single')){
         $('#primary').addClass('read_mode_off');
         $('#read_mode_id').addClass('off');
    }

    //scroll button
    $('body').append('<div title="Scroll to top" class="side_button scroll_top" id="scroll_top"/>');

    $('#scroll_top').click(function(){
       window.scrollTo(0,0);
    });

    if($(window).scrollTop() == 0){
        if($('#read_mode_id').hasClass('off')){
            $('#read_mode_id').css('backgroundPosition','3px -35px');
        }
    }

    $('#follow .google_buzz').css('backgroundPosition', '1px 3px');
    $('#follow .rss').css('backgroundPosition', '3px 50%');
    $('#follow .twitter').css('backgroundPosition', '0 50%');
    $('#follow .youtube').css('backgroundPosition', '3px 20%');
    $('#follow .tumblr').css('backgroundPosition', '0 20%');
    $('.widget_categories .children').hide();

    $('.shareinpost a').hover(function(){
        $(this).find('img').css('background-image','url(/blog-mad/wp-content/plugins/share-and-follow/default/16/sprite-16-color.png)');

    },
    function(){
        $(this).find('img').css('background-image','url(/blog-mad/wp-content/plugins/share-and-follow/default/16/sprite-16.png)');
    });


    $('.widget_categories .cat-item').each(function(){
        if($(this).find('li').length){
            $(this).prepend('<i class="icon-caret-down"/>');
        }
    });

    $('.widget_categories .cat-item').click(

    function(event){
        event.stopPropagation();
        $(this).toggleClass('open');
        //closing
        if(!$(this).hasClass('open')){
            $(this).children('.children').slideUp();
            $(this).children('.icon-caret-up').removeClass('icon-caret-up').addClass('icon-caret-down');
        }
        //opening
        else{
            $(this).children('.children').slideDown();
            $(this).children('.icon-caret-down').removeClass('icon-caret-down').addClass('icon-caret-up');
        }
    }
    );

    $('#read_mode_id').click(function(){
        $(this).toggleClass('off');
        if($(this).hasClass('off')){
            $('#content').removeClass('read_mode_on').addClass('read_mode_off');
            $('#primary').removeClass('read_mode_on').addClass('read_mode_off');
            $(this).attr('title', 'Enable Reading-Mode');
        }
        else{
            $('#content').removeClass('read_mode_off').addClass('read_mode_on');
            $('#primary').removeClass('read_mode_off').addClass('read_mode_on');
            $(this).attr('title', 'Exit Reading-Mode');
        }

    });
    
    if($('#content').hasClass('read_mode_on')){
        $('#read_mode_id').click();
    }

    if($('#read_mode_id').hasClass('off')){
        $('#read_mode_id').attr('title', 'Enable Reading-Mode');
    }
    else{
        $('#read_mode_id').attr('title', 'Exit Reading-Mode');
    }

    //Wrap event bindings - Wait for async js to load
    //    twttr.ready(function (twttr) {
    //        //event bindings
    //        twttr.events.bind('tweet', trackTwitter);
    //    });


    $('.home .share-tab .label').click(function(){
        $(this).parent().toggleClass('open');
    });



});

function trackTwitter(intent_event) {
    if (intent_event) {
        var opt_pagePath;
        if (intent_event.target && intent_event.target.nodeName == 'IFRAME') {
            opt_target = extractParamFromUri(intent_event.target.src, 'url');
        }
        _gaq.push(['_trackSocial', 'twitter', 'tweet', opt_pagePath]);
    }
}

$(window).scroll(function () {

    if($(window).scrollTop()>0){
        //qd on scrolle vers le bas
        $('#follow .feedburner').css('backgroundPosition','-32px 0');
        $('#follow .google_buzz').css('backgroundPosition','-33px 3px');
        $('#follow .rss').css('backgroundPosition','-37px 50%');
        $('#follow .twitter').css('backgroundPosition',' -33px 50% ');
        $('#follow .youtube').css('backgroundPosition',' -36px 20% ');
        $('#follow .tumblr').css('backgroundPosition',' -33px 20% ');
        $('#read_mode_id').css('backgroundPosition','3px 7px');
        $("#scroll_top").fadeIn();
    }

    else{
        //qd on arrive en haut de page
        $('#follow .feedburner').css('backgroundPosition','0 0');
        $('#follow .google_buzz').css('backgroundPosition','1px 3px');
        $('#follow .rss').css('backgroundPosition','3px 50%');
        $('#follow .twitter').css('backgroundPosition','0 50% ');
        $('#follow .youtube').css('backgroundPosition',' 3px 20% ');
        $('#follow .tumblr').css('backgroundPosition',' 0 20%');
        $('#read_mode_id').css('backgroundPosition','3px -35px');
        $("#scroll_top").fadeOut();
    }


    $('#follow .feedburner').hover(
        function(){
            $(this).css('backgroundPosition','0px 0px');
        },
        function(){
            if($(window).scrollTop()>0){
                $(this).css('backgroundPosition','-32px 0');
            }
        }
        );
    $('#follow .google_buzz').hover(
        function(){
            $(this).css('backgroundPosition','1px 3px');
        },
        function(){
            if($(window).scrollTop()>0){
                $(this).css('backgroundPosition','-33px 3px');
            }
        }
        );

    $('#follow .rss').hover(
        function(){
            $(this).css('backgroundPosition','3px 50% ');
        },
        function(){
            if($(window).scrollTop()>0){
                $(this).css('backgroundPosition','-37px 50% ');
            }
        }
        );


    $('#follow .twitter').hover(
        function(){
            $(this).css('backgroundPosition','0 50%');
        },
        function(){
            if($(window).scrollTop()>0){
                $(this).css('backgroundPosition','-33px 50%');
            }
        }
        );

    $('#follow .youtube').hover(
        function(){
            $(this).css('backgroundPosition','3px 20%');
        },
        function(){
            if($(window).scrollTop()>0){
                $(this).css('backgroundPosition','-36px 20%');
            }
        }
        );

    $('#follow .tumblr').hover(
        function(){
            $(this).css('backgroundPosition','0 20%');
        },
        function(){
            if($(window).scrollTop()>0){
                $(this).css('backgroundPosition','-33px 20%');
            }
        }
        );
    $('.single-post #read_mode_id').hover(
        function(){
            $(this).css('backgroundPosition','3px -35px');
        },
        function(){
            if($(window).scrollTop()>0){
                $(this).css('backgroundPosition','3px 7px');
            }
        }
        );


});

function showPortals(){
    $('#follow').append('<div class="portals" />');
    $(window).scroll(function () {
        if($(window).scrollTop()>0){
            $('.portals').css('background-position', '-122px 0');
        }
        else{
            $('.portals').css('background-position', '0 0');
        }

    });
}

