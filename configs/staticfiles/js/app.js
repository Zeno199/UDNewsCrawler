$(document).ready(function() {
    console.log('Hello');
    init();
});

function init() {
    var url = '/news_detail/1'
    function sucHandler(res) {
        var list_html = "<h2>Title"
        //list_html += "<td>" + res['title'] + "</td></h2>" + "<h3>Intro<td>" + res['content'] + "</td></h3>" + "<a href='/webpage/nba_news_detail/" + res['id'] + "/'>Read more...</a>" ;
        //list_html += "<div>-------------------------------------------------------------------------------------------------------------</div>"
        for( var i=0; i < res.length; i++) {
            list_html += "<td>" + res[i].title + "</td></h2>" + "<h3>Intro<td>" + res[i].description + "</td></h3>" + "<a href='/webpage/nba_news_detail/" + res[i].id + "/'>Read more...</a>" ;
            list_html += "<div>-------------------------------------------------------------------------------------------------------------</div>"
        }
        
        $("#news_list").html(list_html);
    };
    function errHandler(res) {window.alert(res)};
    callAJAX_asyc(url, 'get', sucHandler, errHandler)

    /*$('#nba_news_in_focus').click(function() {
        function sucHandler(res) {window.location.reload();window.alert(res.data);};
        function errHandler(res) {window.alert(res)};
        var url = '';
        callAJAX(url, 'post', sucHandler, errHandler);
    });*/
};

function callAJAX_asyc(url, method, sucHandler, errHandler=null) {
    $.ajax({
        url: url,
        type: "GET",
        cache: false,
        data: $(this).serialize(),        
        success: function (res) {
            console.log(data);
            console.log(url);
            console.log(res.data)
            sucHandler(res);
        },
        error: function (res) {
            if (errHandler) {
                console.log(res.data);
                console.log('QQQQQQQQQQQQ');
                console.log(url);
                console.log(res);
                errHandler(res);
            }
        },
        statusCode: {
            403: function(){
                logout_alert_redirect();
            }
        },
        complete: function() {
        },
    });
}

/*function callAJAX(url, method, sucHandler, errHandler=null, data=null) {
    $.ajax({
        url: url,
        type: method,
        cache: false,
        data: data,
        asyn: false,
        success: function (res) {
            console.log(res.data)
            sucHandler(res);
        },
        error: function (res) {
            if (errHandler) {
                errHandler(res);
            }
        },
        statusCode: {
            403: function(){
                logout_alert_redirect();
            }
        },
        complete: function() {
        },
    });
}*/
