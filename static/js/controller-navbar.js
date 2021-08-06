function preloaderShowQS(){
    $('#maincon').fadeOut('fast');
    $('loader').show();
    $('#PreLoaderBar').show();
    $('quickstory').toggle("slide", {direction:'down'});
}

function preloaderShowMain(){
    $('#maincon').fadeOut('fast');
    $('loader').show();
    $('#PreLoaderBar').show();
}

function comingSoon(){
    new jBox('Notice', {
        content: 'Coming Soon',
        color: 'red',
    });
}

function changeUsername(element,username){
    var URL = $(element).attr('render-url');
    var USERNAME = $(username).val();
    $.ajax({
        url: URL,
        type: "POST",
        dataType: "html",
        data: {
            'ajax.render':'username.change',
            'username.change.input':USERNAME,
            'csrfmiddlewaretoken': CSRFTOKENNAV,
        },
        success: function(result){
            if(result == '1'){
                window.open('','_SELF');
            }
        }
    });
}

function confirmEmail(element){
    function refreshEmail(url){
        $.ajax({
            url: url,
            type: "POST",
            dataType: "html",
            data: {
                'ajax.render':'email.place.render',
                'csrfmiddlewaretoken': CSRFTOKENNAV,
            },
            success: function(result){
                $('#emailContainer').html(result);
            }
        });
    }
    $('#PreLoaderBar').show();
    var REQ_NAME = $(element).attr('render');
    var TITLE  = $(element).attr('render-name');
    var URL = $(element).attr('render-url');
    $.ajax({
        url: URL,
        type: "POST",
        dataType: "html",
        data: {
            'ajax.render':REQ_NAME,
            'emailConfirm':$('#emailConfirm').val(),
            'csrfmiddlewaretoken': CSRFTOKENNAV,
        },
        success: function(result){
            if(result == '#'){
                let src = 'https://cdn.tell.by/sound/effect/ok.wav';
                let audio = new Audio(src);
                audio.play();
                new jBox('Notice', {
                    content: 'Confirmation Sent!',
                    color: 'black',
                });
                refreshEmail(URL);
                $('#PreLoaderBar').hide();
            }else if(result == '&'){
                $('#PreLoaderBar').hide();
                let src = 'https://cdn.tell.by/sound/effect/error.wav';
                let audio = new Audio(src);
                audio.play();
                new jBox('Notice', {
                    content: "we've already sent the verification!",
                    color: 'red',
                });
                setTimeout(function(){
                    new jBox('Notice', {
                        content: 'Check/Change your Email!',
                        color: 'red',
                    });
                },1000);
            }else if(result == '*'){
                $('#PreLoaderBar').hide();
                let src = 'https://cdn.tell.by/sound/effect/error.wav';
                let audio = new Audio(src);
                audio.play();
                new jBox('Notice', {
                    content: "Email in use",
                    color: 'red',
                });
            }else if(result == '@'){
                $('#PreLoaderBar').hide();
                let src = 'https://cdn.tell.by/sound/effect/error.wav';
                let audio = new Audio(src);
                audio.play();
                new jBox('Notice', {
                    content: "You are using this email.",
                    color: 'red',
                });
            }else if(result == '%'){
                let src = 'https://cdn.tell.by/sound/effect/ok.wav';
                let audio = new Audio(src);
                audio.play();
                new jBox('Notice', {
                    content: 'Email Changed!',
                    color: 'black',
                });
                setTimeout(function(){
                    new jBox('Notice', {
                        content: 'Confirmation Sent!',
                        color: 'black',
                    });
                },1000);
                refreshEmail(URL);
                $('#PreLoaderBar').hide();
            }else{
                let src = 'https://cdn.tell.by/sound/effect/error.wav';
                let audio = new Audio(src);
                audio.play();
                new jBox('Notice', {
                    content: 'Error',
                    color: 'red',
                });
                $('#PreLoaderBar').hide();
            }
        }
    });
}


/* SPERATED FUNCTION OMNI PAGE!*/
function getPages(element){
    $('#maincon').fadeOut('fast');
    $('loader').show();
    $('#PreLoaderBar').show();
    var REQ_NAME = $(element).attr('render');
    var TITLE  = $(element).attr('render-name');
    var URL = $(element).attr('render-url');
    document.title = TITLE;
    window.history.pushState('tellby', TITLE, URL);
    $.ajax({
        url: URL,
        type: "POST",
        dataType: "html",
        data: {
            'ajax.render':REQ_NAME,
            'csrfmiddlewaretoken': CSRFTOKENNAV,
        },
        success: function(result){
            if(result != '0'){
                $('#PreLoaderBar').hide();
                $('loader').hide();
                $('#maincon').html(result);
                $('#maincon').fadeIn('fast');
            }else{
                let src = 'https://cdn.tell.by/sound/effect/error.wav';
                let audio = new Audio(src);
                audio.play();
                new jBox('Notice', {
                    content: 'Error',
                    color: 'red',
                });
                $('#PreLoaderBar').hide();
                $('loader').hide();
                $('#maincon').fadeIn('fast');
            }
        }
    });
}


function getModal(element){
    var REQ_NAME = $(element).attr('render');
    var URL = $(element).attr('render-url');
    var SUBPAGES = $(element).attr('render-sub');
    $('#PreLoaderBar').show();
    $.ajax({
        url: URL,
        type: "POST",
        dataType: "html",
        data: {
            'ajax.render':REQ_NAME,
            'csrfmiddlewaretoken': CSRFTOKENNAV,
        },
        success: function(result){
            if(result != '0'){
                $('#PreLoaderBar').hide();
                $(SUBPAGES).html(result);
            }else{
                let src = 'https://cdn.tell.by/sound/effect/error.wav';
                let audio = new Audio(src);
                audio.play();
                new jBox('Notice', {
                    content: 'Error',
                    color: 'red',
                });
                $('#PreLoaderBar').hide();
            }
        }
    });
}

function getSubPages(element){
    var REQ_NAME = $(element).attr('render');
    var TITLE  = $(element).attr('render-name');
    var URL = $(element).attr('render-url');
    var SUBPAGES = $(element).attr('render-sub');

    $(SUBPAGES).fadeOut('fast');
    $('#PreLoaderBar').show();
    if(TITLE){
        document.title = TITLE;
        window.history.pushState('tellby', TITLE, URL);
    }
    $.ajax({
        url: URL,
        type: "POST",
        dataType: "html",
        data: {
            'ajax.render':REQ_NAME,
            'csrfmiddlewaretoken': CSRFTOKENNAV,
        },
        success: function(result){
            if(result != '0'){
                $('#PreLoaderBar').hide();
                $(SUBPAGES).html(result);
                $(SUBPAGES).fadeIn('fast');
            }else{
                let src = 'https://cdn.tell.by/sound/effect/error.wav';
                let audio = new Audio(src);
                audio.play();
                new jBox('Notice', {
                    content: 'Error',
                    color: 'red',
                });
                $('#PreLoaderBar').hide();
                $(SUBPAGES).fadeIn('fast');
            }
        }
    });
}


function loadMore(element) {
    $(element).fadeOut('slow');
    $('#PreLoaderBar').show();
    var next_page = $(element).attr('load-more-data');
    var ajax_defined = $(element).attr('load');
    setTimeout(function(){
        $(element).remove();
    },1000);
    setTimeout(function(){
        var LoadContainer = $('.load-container').html();
        $.ajax({
            url: '.',
            type: "POST",
            dataType: "html",
            data: {
                'ajax.render':ajax_defined,
                'p':next_page,
                'csrfmiddlewaretoken': CSRFTOKENNAV,
            },
            success: function(result){
                $('#PreLoaderBar').hide();
                $('loader').hide();
                $('.load-container').html(LoadContainer+result);
                console.log(next_page);
            }
        });
    },1500);
};

function deleteStory(element){
    $('#maincon').fadeOut('fast');
    $('loader').show();
    $('#PreLoaderBar').show();
    var REQ_NAME = $(element).attr('render');
    var TITLE  = $(element).attr('render-name');
    var URL = $(element).attr('render-url');
    document.title = TITLE;
    var NEWURL = URL.replace("delete/", "");
    window.history.pushState('Deleting Post', TITLE, NEWURL);
    $.ajax({
        url: URL,
        type: "POST",
        dataType: "html",
        data: {
            'ajax.render':REQ_NAME,
            'csrfmiddlewaretoken': CSRFTOKENNAV,
        },
        success: function(result){
            if(result != '0'){
                let src = 'https://cdn.tell.by/sound/effect/ok.wav';
                let audio = new Audio(src);
                audio.play();
                new jBox('Notice', {
                    content: 'story deleted!',
                    color: 'black',
                });
                document.title = 'Delete Success';
                window.history.pushState('Deleting Post', '', NEWURL);
                $('#PreLoaderBar').hide();
                $('loader').hide();
                $('#maincon').html(result);
                $('#maincon').fadeIn('fast');
            }else{
                window.history.pushState('Deleting Post', '', NEWURL);
                document.title = 'Showing Original Post';
                let src = 'https://cdn.tell.by/sound/effect/error.wav';
                let audio = new Audio(src);
                audio.play();
                new jBox('Notice', {
                    content: 'Failed!!',
                    color: 'red',
                });
                $.ajax({
                    url: NEWURL,
                    type: "POST",
                    dataType: "html",
                    data: {
                        'ajax.render':'story.view.render',
                        'csrfmiddlewaretoken': CSRFTOKENNAV,
                    },
                    success: function(result){
                        $('#PreLoaderBar').hide();
                        $('loader').hide();
                        $('#maincon').html(result);
                        $('#maincon').fadeIn('fast');
                    }
                });
            }
        }
    });
}


function editStory(element){
    var REQ_NAME = $(element).attr('render');
    var URL = $(element).attr('render-url');
    var SUBPAGES = $(element).attr('render-sub');
    var NEWURL = URL.replace("edit/", "");
    $(SUBPAGES).fadeOut('fast');
    $('#PreLoaderBar').show();
    $.ajax({
        url: URL,
        type: "POST",
        dataType: "html",
        data: {
            'ajax.render':REQ_NAME,
            'csrfmiddlewaretoken': CSRFTOKENNAV,
        },
        success: function(result){
            if(result != '0'){
                new jBox('Notice', {
                    content: 'Load Editor...',
                    color: 'black',
                });
                $('#PreLoaderBar').hide();
                $(SUBPAGES).html(result);
                $(SUBPAGES).fadeIn('fast');
            }else{
                let src = 'https://cdn.tell.by/sound/effect/error.wav';
                let audio = new Audio(src);
                audio.play();
                new jBox('Notice', {
                    content: 'Please confirm your EMAIL!',
                    color: 'red',
                });
                $('#PreLoaderBar').hide();
                $(SUBPAGES).fadeIn('fast');
            }
        }
    });
}

function saveStory(element,title,keyword,tiny){
    var CONTENT =  tinyMCE.get(tiny).getContent();
    if(CONTENT){
        new jBox('Notice', { content: 'Saving...', color: 'black', });
        var KEYWORD = $(keyword).val();
        var TITLE = $(title).val();
        var REQ_NAME = $(element).attr('render');
        var URL = $(element).attr('render-url');
        var SUBPAGES = $(element).attr('render-sub');
        var NEWURL = $(element).attr('main-url');
        var CONTENTTYPE = $(element).attr('tinywhat');
        $('#PreLoaderBar').show();
        $.ajax({
            url: URL,
            type: "POST",
            dataType: "html",
            data: {
                'ajax.render':REQ_NAME,
                'content-validator':CONTENTTYPE,
                'content':CONTENT,
                'content-title':TITLE,
                'content-keyword':KEYWORD,
                'csrfmiddlewaretoken': CSRFTOKENNAV,
            },
            success: function(result){
                if(result == '0'){
                    let src = 'https://cdn.tell.by/sound/effect/error.wav';
                    let audio = new Audio(src);
                    audio.play();
                    new jBox('Notice', {
                        content: 'Failed!',
                        color: 'red',
                    });
                    $('#PreLoaderBar').hide();
                    $(SUBPAGES).fadeIn('fast');
                }else{
                    tinymce.remove();
                    let src = 'https://cdn.tell.by/sound/effect/ok.wav';
                    let audio = new Audio(src);
                    audio.play();
                    new jBox('Notice', {
                        content: 'Done...',
                        color: 'black',
                    });
                    $('#maincon').fadeOut('fast');
                    $('loader').show();
                    var RE_NAME = 'story.view.render';
                    $.ajax({
                        url: NEWURL,
                        type: "POST",
                        dataType: "html",
                        data: {
                            'ajax.render':RE_NAME,
                            'csrfmiddlewaretoken': CSRFTOKENNAV,
                        },
                        success: function(result){
                            $('#PreLoaderBar').hide();
                            document.title = TITLE;
                            $('loader').hide();
                            $('#maincon').html(result);
                            $('#maincon').fadeIn('fast');
                        }
                    });
                }
            }
        });
    }else{
        let src = 'https://cdn.tell.by/sound/effect/error.wav';
        let audio = new Audio(src);
        audio.play();
        new jBox('Notice', {
            content: 'Empty!',
            color: 'red',
        });
    }
}

function createStory(element,title,keyword,tiny){
    var CONTENT =  tinyMCE.get(tiny).getContent();
    if(CONTENT){
        new jBox('Notice', { content: 'Saving...', color: 'black', });
        var KEYWORD = $(keyword).val();
        var TITLE = $(title).val();
        var REQ_NAME = $(element).attr('render');
        var URL = $(element).attr('render-url');
        var SUBPAGES = $(element).attr('render-sub');
        var NEWURL = $(element).attr('main-url');
        var CONTENTTYPE = $(element).attr('tinywhat');
        $('#PreLoaderBar').show();
        $.ajax({
            url: URL,
            type: "POST",
            dataType: "html",
            data: {
                'ajax.render':REQ_NAME,
                'content-validator':CONTENTTYPE,
                'content':CONTENT,
                'content-title':TITLE,
                'content-keyword':KEYWORD,
                'csrfmiddlewaretoken': CSRFTOKENNAV,
            },
            success: function(result){
                if(result == '0'){
                    let src = 'https://cdn.tell.by/sound/effect/error.wav';
                    let audio = new Audio(src);
                    audio.play();
                    new jBox('Notice', {
                        content: 'Failed!',
                        color: 'red',
                    });
                    $('#PreLoaderBar').hide();
                    $(SUBPAGES).fadeIn('fast');
                }else if(result == '9'){
                    let src = 'https://cdn.tell.by/sound/effect/error.wav';
                    let audio = new Audio(src);
                    audio.play();
                    new jBox('Notice', {
                        content: 'Please confirm your EMAIL.',
                        color: 'red',
                    });
                    $('#PreLoaderBar').hide();
                    $(SUBPAGES).fadeIn('fast');
                }else{
                    new jBox('Notice', { content: 'Getting data...', color: 'black', });
                    tinymce.get(tiny).setContent('');
                    tinymce.remove();
                    $(title).val('');
                    $(keyword).val('');
                    $('#maincon').fadeOut('fast');
                    $('loader').show();
                    var NEWURL = result.replace("3LL:", "");
                    var GETURL = '/p/'+NEWURL+'/';
                    if(TITLE){
                        var TITLEOK = TITLE;
                    }else{
                        var TITLEOK = 'Story';
                    }
                    document.title = TITLEOK;
                    window.history.pushState('tellby', TITLEOK, GETURL);

                    $.ajax({
                        url: GETURL,
                        type: "POST",
                        dataType: "html",
                        data: {
                            'ajax.render':'story.view.render',
                            'csrfmiddlewaretoken': CSRFTOKENNAV,
                        },
                        success: function(data){
                            if(data != '0'){
                                let src = 'https://cdn.tell.by/sound/effect/ok.wav';
                                let audio = new Audio(src);
                                audio.play();
                                new jBox('Notice', { content: 'Done...', color: 'black', });
                                $('#PreLoaderBar').hide();
                                $('loader').hide();
                                $('#maincon').html(data);
                                $('#maincon').fadeIn('fast');
                            }else{
                                let src = 'https://cdn.tell.by/sound/effect/error.wav';
                                let audio = new Audio(src);
                                audio.play();
                                new jBox('Notice', {
                                    content: 'Error',
                                    color: 'red',
                                });
                                $('#PreLoaderBar').hide();
                                $('loader').hide();
                                $('#maincon').fadeIn('fast');
                            }
                        }
                    });
                }
            }
        });
    }else{
        let src = 'https://cdn.tell.by/sound/effect/error.wav';
        let audio = new Audio(src);
        audio.play();
        new jBox('Notice', {
            content: 'Empty!',
            color: 'red',
        });
    }
}



/*
 * jQuery Function Toggle Pluing
 * Copyright 2011, Felix Kling
 * Dual licensed under the MIT or GPL Version 2 licenses.
 */
;(function (factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define(['jquery'], factory);
    } else {
        // Browser globals
        factory(jQuery);
    }
}) (function($) {
    $.fn.funcToggle = function(type, data) {
        var dname = "jqp_eventtoggle_" + type + (new Date()).getTime(),            
            funcs = Array.prototype.slice.call(arguments, 2),
            numFuncs = funcs.length,
            empty = function() {},
            false_handler = function() {return false;};

        if(typeof type === "object") {
            for( var key in type) {
                $.fn.funcToggle.apply(this, [key].concat(type[key]));
            }
            return this;
        }
        if($.isFunction(data) || data === false) {
            funcs = [data].concat(funcs);
            numFuncs += 1;
            data = undefined;
        }

        funcs = $.map(funcs, function(func) {
            if(func === false) {
                return false_handler;
            }
            if(!$.isFunction(func)) {
                return empty;
            }
            return func;
        });

        this.data(dname, 0);
        this.bind(type, data, function(event) {
            var data = $(this).data(),
                index = data[dname];
            funcs[index].call(this, event);
            data[dname] = (index + 1) % numFuncs;
        });
        return this;
    };
});
