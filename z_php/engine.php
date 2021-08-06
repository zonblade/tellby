<?php
/* image profile */

/*image for web*/
if(isset($_GET['web_icon'])){
    $filename = $_GET['web_icon'];
    $filePath_try_to_download = "../static/img/icon/$filename";
    if(file_exists($filePath_try_to_download))
    {
        $filename = strtolower(substr(strrchr($filename,"."),1));
        switch( $file_extension ) {
            case "gif": $ctype="image/gif"; break;
            case "png": $ctype="image/png"; break;
            case "svg": $ctype="image/svg"; break;
            case "jpeg":
            case "jpg": $ctype="image/jpeg"; break;
            case "svg": $ctype="image/svg+xml"; break;
            default:
        }

        $fileSize = filesize($filePath_try_to_download);
        header("Cache-Control: private");
        header('Content-type: ' . $ctype);
        header("Content-Length: ".$fileSize);
        header("Content-Disposition: inline; filename=$filename");
        // Output file.
        readfile ($filePath_try_to_download);
        exit();
    }else{
        readfile ('./cdn.html');
    };
}

/*image for web*/
if(isset($_GET['avatar'])){
    $filename = $_GET['avatar'];
    $filePath_try_to_download = "../static/img/avatar/$filename";
    if(file_exists($filePath_try_to_download))
    {
        $filename = strtolower(substr(strrchr($filename,"."),1));
        switch( $file_extension ) {
            case "gif": $ctype="image/gif"; break;
            case "png": $ctype="image/png"; break;
            case "svg": $ctype="image/svg"; break;
            case "jpeg":
            case "jpg": $ctype="image/jpeg"; break;
            case "svg": $ctype="image/svg+xml"; break;
            default:
        }

        $fileSize = filesize($filePath_try_to_download);
        header("Cache-Control: private");
        header('Content-type: ' . $ctype);
        header("Content-Length: ".$fileSize);
        header("Content-Disposition: inline; filename=$filename");
        // Output file.
        readfile ($filePath_try_to_download);
        exit();
    }else{
        readfile ('./cdn.html');
    };
}


/*image for web*/
if(isset($_GET['story_img'])){
    $filename = $_GET['story_img'];
    $filePath_try_to_download = "../static/img/story/$filename";
    if(file_exists($filePath_try_to_download))
    {
        $filename = strtolower(substr(strrchr($filename,"."),1));
        switch( $file_extension ) {
            case "gif": $ctype="image/gif"; break;
            case "png": $ctype="image/png"; break;
            case "jpeg":
            case "jpg": $ctype="image/jpeg"; break;
            case "svg": $ctype="image/svg+xml"; break;
            default:
        }

        $fileSize = filesize($filePath_try_to_download);
        header("Cache-Control: private");
        header('Content-type: ' . $ctype);
        header("Content-Length: ".$fileSize);
        header("Content-Disposition: inline; filename=$filename");
        // Output file.
        readfile ($filePath_try_to_download);
        exit();
    }else{
        readfile ('./cdn.html');
    };
}
