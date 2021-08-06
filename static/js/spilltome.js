/* SPERATED FUNCTION OMNI PAGE!*/
function getPages(element){
    var REQ_NAME = $(element).attr('agung');
    var TITLE  = $(element).attr('agung-name');
    var URL = $(element).attr('agung-url');
    document.title = TITLE;
    window.history.pushState('Agung', TITLE, URL);
    new jBox("Notice", {
        theme: "NoticeFancy",
        attributes: {
            x: "left",
            y: "top"
        },
        color: 'black',
        content: "Loading...",
        animation: {
            open: "slide:top",
            close: "slide:left"
        }
    })
    $('#mainbody').fadeOut('fast');
    setTimeout(function(){
        $('loader').show();
    },400);
    setTimeout(function(){
        $.ajax({
            url: URL,
            method: "POST",
            dataType: "html",
            data: {
                'ajax.render':REQ_NAME,
                'csrfmiddlewaretoken': CSRFTOKENNAV,
            },
            success: function(result){
                if(result != '0'){
                    //$('loader').hide();
                    new jBox("Notice", {
                        theme: "NoticeFancy",
                        attributes: {
                            x: "left",
                            y: "top"
                        },
                        color: 'green',
                        content: TITLE+" Loaded...",
                        audio: "https://cdn.jsdelivr.net/gh/StephanWagner/jBox@latest/assets/audio/bling2",
                        volume: 80,
                        animation: {
                            open: "slide:top",
                            close: "slide:left"
                        }
                    })
                    $('#mainbody').html(result);
                    $('#mainbocy').waitForImages(function(){
                        $('loader').hide();
                        $('#mainbody').fadeIn('fast');
                    })
                }else{
                    new jBox('Notice', {
                        content: 'Error',
                        color: 'red',
                    });
                    //$('loader').hide();
                    //$('#mainbody').fadeIn('fast');
                }
            }
        });
    },500);
}

