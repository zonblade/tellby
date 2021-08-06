new jBox('Tooltip', {
    theme: 'TooltipDark',
    attach: '.tooltp',
    delayOpen: 50,
    delayClose: 100
});
$('html').waitForImages( function(){
    $('.img_loader').hide();
    setTimeout(function(){
        $('#users').show().addClass('animate__animated animate__fadeIn');
    },500);
})
