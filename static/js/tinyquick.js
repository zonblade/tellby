
var useDarkMode = window.matchMedia('(prefers-color-scheme: oxide-dark)').matches;

tinymce.init({
    selector: '#quickstorytext',
    oninit : "setPlainText",
    plugins: 'paste fullscreen image link wordcount quickbars anchor',
    menubar: false,
    resize:true,
    entity_encoding : "raw",
    paste_as_text: true,
    image_advtab: true,
    image_dimensions: false,
    image_class_list: [
        {title: 'Fluid Only', value: 'img-fluid'}
    ],
    quickbars_insert_toolbar: '',
    quickbars_selection_toolbar: 'forecolor backcolor | bold italic underline strikethrough | quicklink h2 h3 blockquote',
    toolbar: 'fullscreen | undo redo | bold italic | alignleft aligncenter alignright alignjustify | image anchor',
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:0.8rem } img{max-width:100%;}',
    skin: (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'oxide-dark' : 'oxide'),
    content_css: (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'default'),
});
