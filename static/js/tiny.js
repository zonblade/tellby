
var useDarkMode = window.matchMedia('(prefers-color-scheme: oxide-dark)').matches;

tinymce.init({
    selector: 'textarea',
    plugins: 'print preview paste importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen image link template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists wordcount imagetools textpattern noneditable help charmap quickbars emoticons',
    imagetools_cors_hosts: ['picsum.photos'],
    menubar: 'file edit view insert format tools table help',
    toolbar: ' fullscreen  preview | undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | insertfile image template link anchor codesample | ltr rtl',
    autosave_ask_before_unload: true,
    autosave_interval: '30s',
    autosave_prefix: '{path}{query}-{id}-',
    autosave_restore_when_empty: false,
    autosave_retention: '2m',
    image_advtab: true,
    image_dimensions: false,
    image_class_list: [
        {title: 'Fluid FullSize', value: 'img-fluid img-story'},
        {title: 'Fluid Only', value: 'img-fluid'}
    ],
    quickbars_insert_toolbar: '',
    importcss_append: true,
    image_caption: true,
    quickbars_selection_toolbar: 'forecolor backcolor | bold italic underline strikethrough | quicklink h2 h3 blockquote quicktable',
    noneditable_noneditable_class: 'mceNonEditable',
    toolbar_mode: 'sliding',
    contextmenu: 'link image imagetools table',
    skin: (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'oxide-dark' : 'oxide'),
    content_css: (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'default'),
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px } img { border-radius: 10px !important; width:100% !important; }'
});


/*tinymce.init({
    selector: 'textarea',
    plugins: 'searchreplace image link paste',
    paste_as_text: true,
    toolbar_mode: 'floating',
    content_style : 'img { border-radius: 10px !important; width:100% !important; }',
    image_dimensions: false,
    image_class_list: [
        {title: 'Fluid FullSize', value: 'img-fluid img-story'},
        {title: 'Fluid Only', value: 'img-fluid'}
    ]
});*/