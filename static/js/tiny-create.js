var useDarkMode = window.matchMedia('(prefers-color-scheme: oxide-dark)').matches;

new jBox('Notice', {
    content: 'Load Editor',
    color: 'black',
});
var edit = {
    selector: '#editXthebox',
    menubar: false,
    skin: 'oxide-dark',
    content_css: 'dark',
    inline: true,
    plugins: [
        'autolink',
        'codesample',
        'link',
        'lists',
        'media',
        'table',
        'image',
        'quickbars',
        'codesample',
        'help'
    ],
    image_advtab: true,
    image_dimensions: false,
    image_class_list: [
        {title: 'Fluid Only', value: 'img-fluid'}
    ],
    toolbar: false,
    quickbars_insert_toolbar: 'quicktable image codesample',
    quickbars_selection_toolbar: 'bold italic underline | formatselect | blockquote quicklink',
    contextmenu: 'undo redo | inserttable | cell row column deletetable | help',
    powerpaste_word_import: 'clean',
    powerpaste_html_import: 'clean',
}

tinymce.init(edit).then(function(afterload) {
    $('#editorloader').remove();
    $('#editXthebox').fadeIn('slow');
    let src = 'https://cdn.tell.by/sound/effect/ok.wav';
    let audio = new Audio(src);
    audio.play();
    new jBox('Notice', {
        content: 'Editor Loaded...',
        color: 'black',
    });
});