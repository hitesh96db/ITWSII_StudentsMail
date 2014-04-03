//Scripts to load sharing widgets
//gplus
(function() {
    var po = document.createElement('script');
    po.type = 'text/javascript';
    po.async = true;
    po.src = 'https://apis.google.com/js/plusone.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(po, s);
})();
    
//twitter
(function(d,s,id){
    var js,fjs=d.getElementsByTagName(s)[0];
    if(!d.getElementById(id)){
        js=d.createElement(s);
        js.id=id;
        js.src="https://platform.twitter.com/widgets.js";
        fjs.parentNode.insertBefore(js,fjs);
    }
})(document,"script","twitter-wjs");
    
//Fb
/*(function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s);
        js.id = id;
        js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));*/
    
//stumbleupon
(function() {
    var li = document.createElement('script');
    li.type = 'text/javascript';
    li.async = true;
    li.src = ('https:' == document.location.protocol ? 'https:' : 'http:') + '//platform.stumbleupon.com/1/widgets.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(li, s);
})();

//hacker news
(function(d, t) {
    var g = d.createElement(t),
        s = d.getElementsByTagName(t)[0];
    g.src = '//hnbutton.appspot.com/static/hn.min.js';
    s.parentNode.insertBefore(g, s);
}(document, 'script'));

(function($, window){
    $('.post').each(function(){
       var hn = $(this).find('.hacker_news a').clone(),
            span = $('<span class="social_widget_embedded"/>');
            span.append(hn);
       $(this).find('.entry-meta').append(span);
    });
}(jQuery, this));

/*Social tracking*****************************************************************************************************************/
var _gaq = _gaq || [];

function trackTwitter(intent_event) {
    if (intent_event) {
        var opt_pagePath;
        if (intent_event.target && intent_event.target.nodeName == 'IFRAME') {
            opt_target = extractParamFromUri(intent_event.target.src, 'url');
        }
        _gaq.push(['_trackSocial', 'twitter', 'tweet', opt_pagePath]);
    }
}
  
function extractParamFromUri(uri, paramName) {
    if (!uri) {
        return;
    }
    var regex = new RegExp('[\\?&#]' + paramName + '=([^&#]*)');
    var params = regex.exec(uri);
    if (params != null) {
        return unescape(params[1]);
    }
    return;
}

//Wrap event bindings - Wait for async js to load
/*twttr.ready(function (twttr) {
    //event bindings
    twttr.events.bind('tweet', trackTwitter);
});*/