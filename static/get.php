<?php

include '../config.php';


if(isset($_GET['commonword'])){
    error_reporting(E_ALL);
    ini_set('display_errors', 'On');
    if($_GET['commonword'] == 'month'){
        $res = $mysqli->query("SELECT * FROM `postingan_postingan`");
        $text ='';
        while ($row_users = $res->fetch_array()) {
            //output a row here
            $years = date("m", strtotime($row_users['post_date']));
            $years_now = date("m");
            if($years == $years_now){
                $text .= strip_tags($row_users['content'])."";
            }
        }

        $regex = '~(#\w+)~';
        $matches = '#';
        if (preg_match_all($regex, $text, $matches, PREG_PATTERN_ORDER)) {
            foreach ($matches[1] as $word) {
                echo $word .' ';
            }
        }
    }
    if($_GET['commonword'] == 'alltime'){
        $res = $mysqli->query("SELECT * FROM `postingan_postingan`");
        $text ='';
        while ($row_users = $res->fetch_array()) {
            //output a row here
            $years = date("m", strtotime($row_users['post_date']));
            $years_now = date("m");
            $text .= strip_tags($row_users['content'])."";
        }

        $regex = '~(#\w+)~';
        $matches = '#';
        if (preg_match_all($regex, $text, $matches, PREG_PATTERN_ORDER)) {
            foreach ($matches[1] as $word) {
                echo $word .' ';
            }
        }
    }
    if($_GET['commonword'] == 'Xall'){
        $res = $mysqli->query("SELECT * FROM `postingan_postingan`");
        $text ='';
        while ($row_users = $res->fetch_array()) {
            //output a row here
            $years = date("m", strtotime($row_users['post_date']));
            $years_now = date("m");
            $text .= strip_tags($row_users['content'])."";
        }

        $regex = '~(#\w+)~';
        $matches = '#';
        if (preg_match_all($regex, $text, $matches, PREG_PATTERN_ORDER)) {
            foreach ($matches[1] as $word) {
                echo $word .' ';
            }
        }
    }
    die();
}


if(isset($_GET['popularpost'])){
    error_reporting(E_ALL);
    ini_set('display_errors', 'On');
    $res = $mysqli->query("SELECT * FROM `postingan_postingan` ORDER BY `post_seen` DESC LIMIT 10");
    $text ='';
    while ($row_users = $res->fetch_array()) {
        //output a row here
        echo "(".strip_tags($row_users['mock_url']).")";
    }
    die();
}

if(isset($_GET['js'])){
    $filename = $_GET['js'];
    $filePath_try_to_download = __DIR__."/js/$filename";
    if(file_exists($filePath_try_to_download))
    {
        $fileSize = filesize($filePath_try_to_download);
        header("Cache-Control: private");
        header('Content-type: text/javascript');
        header("Content-Length: ".$fileSize);
        header("Content-Disposition: inline; filename=$filename");
        // Output file.
        readfile ($filePath_try_to_download);
        exit();
    }else{
        readfile ('./cdn.html');
    };
}


if(isset($_GET['css'])){
    $filename = $_GET['css'];
    $filePath_try_to_download = __DIR__."/css/$filename";
    if(file_exists($filePath_try_to_download))
    {
        $fileSize = filesize($filePath_try_to_download);
        header("Cache-Control: private");
        header('Content-type: text/css');
        header("Content-Length: ".$fileSize);
        header("Content-Disposition: inline; filename=$filename");
        // Output file.
        readfile ($filePath_try_to_download);
        exit();
    }else{
        readfile ('./cdn.html');
    };
}

function THIS_IS_AVATAR_PRINT(){}
if(isset($_GET['avatar'])){
    $filename = $_GET['avatar'];
    $filename_2 = "cape.png";
    $filePath_try_to_download = __DIR__."/img/avatar/user/$filename.png";
    $filePath_try_to_download_2 = __DIR__."/img/avatar/cape.png";
    $file_extension = substr($filename, strpos($filename, ".") + 1); 
    $file_extension_2 = substr($filename_2, strpos($filename_2, ".") + 1); 
    if(file_exists($filePath_try_to_download))
    {
        $image = new Imagick();
        $image->readImage($filePath_try_to_download);
        $image->setImageCompression(Imagick::COMPRESSION_JPEG);
        $image->setImageCompressionQuality(25);
        header("Content-Type: image/" . $image->getImageFormat());
        echo $image;
    }else{
        $image = new Imagick();
        $image->readImage($filePath_try_to_download_2);
        $image->setImageCompression(Imagick::COMPRESSION_JPEG);
        $image->setImageCompressionQuality(1);
        header("Content-Type: image/" . $image->getImageFormat());
        echo $image;
    };
}

function THIS_IS_IMAGE_UPLOAD(){}
if(isset($_GET['serverkey'])){
    if($_GET['serverkey'] == 'dumdum'){
        if(isset($_POST['secretkey'])){
            if($_POST['secretkey'] == '???'){ /** remove secret key */
                if(!empty($_FILES['upfile']['name'])){
                    $img_nm = $_POST['secret_username'];
                    $image = new Imagick();
                    $image->readImage($_FILES['upfile']['tmp_name']);
                    $cropWidth = $image->getImageWidth();
                    $cropHeight = $image->getImageHeight();
                    if($cropHeight > 4000){
                        $newWidth = $cropWidth / 4;
                        $newHeight = $cropHeight / 4;
                    }elseif($cropHeight > 2000){
                        $newWidth = $cropWidth / 3;
                        $newHeight = $cropHeight / 3;
                    }elseif($cropHeight > 1000){
                        $newWidth = $cropWidth / 2;
                        $newHeight = $cropHeight / 2;
                    }else{
                        $newWidth = $cropWidth / 2;
                        $newHeight = $cropHeight / 2;
                    }
                    $image->resizeImage($newWidth,$newHeight,Imagick::FILTER_LANCZOS,1);
                    $image->compositeimage($image, Imagick::COMPOSITE_OVER, 0, 0);
                    $image->setImageFormat('jpg');
                    $image->setImageCompression(Imagick::COMPRESSION_JPEG);
                    $image->setImageCompressionQuality(20);
                    file_put_contents (__DIR__."/img/avatar/user/".$img_nm.".png", $image);
                }
            }
            else{
                echo 'wrong key'.$_FILES["upfile"]["name"];
            }
        }
        else{
            echo 'no scret key'.$_FILES["upfile"]["name"];
        }
    }else{
        echo 'wrong key';
    }
}



function THISISIMAGEIPLOADFORGALLERY(){}
if(isset($_GET['serverkey'])){
    if($_GET['serverkey'] == 'petrodactyl'){
        if(isset($_POST['secretkey'])){
            if($_POST['secretkey'] == '???'){ /** remove secret key */
                if(!empty($_FILES['upfile']['name'])){
                    $img_nm = $_POST['image_name_hash'];
                    $image = new Imagick();
                    $image->readImage($_FILES['upfile']['tmp_name']);
                    $cropWidth = $image->getImageWidth();
                    $cropHeight = $image->getImageHeight();
                    if($cropHeight > 4200){
                        $newWidth = $cropWidth / 3.2;
                        $newHeight = $cropHeight / 3.2;
                    }elseif($cropHeight > 3000){
                        $newWidth = $cropWidth / 2.5;
                        $newHeight = $cropHeight / 2.5;
                    }elseif($cropHeight > 1600){
                        $newWidth = $cropWidth / 1.5;
                        $newHeight = $cropHeight / 1.5;
                    }else{
                        $newWidth = $cropWidth / 1.1;
                        $newHeight = $cropHeight / 1.1;
                    }
                    $image->resizeImage($newWidth,$newHeight,Imagick::FILTER_LANCZOS,1);
                    $image->compositeimage($image, Imagick::COMPOSITE_OVER, 0, 0);
                    $image->setImageFormat('jpg');
                    $image->setImageCompression(Imagick::COMPRESSION_JPEG);
                    $image->setImageCompressionQuality(20);
                    file_put_contents (__DIR__."/img/galeri/".$img_nm.".jpg", $image);
                }
            }
            else{
                echo 'wrong key'.$_FILES["upfile"]["name"];
            }
        }
        else{
            echo 'no scret key'.$_FILES["upfile"]["name"];
        }
    }else{
        echo 'wrong key';
    }
}


function IMAGE_PRINT_BELOW_WITH_WATERMARK(){}
if(isset($_GET['img'])){
    if(file_exists(__DIR__.'/img/galeri/'.$_GET['img'].'.jpg')):
    #SELECT FROM DATABASE BY IMC MOCKED!!!
    $res = $mysqli->query("SELECT * FROM `gallery_image_gallery` WHERE `img_name` = '".$_GET['img']."'");
    $res_id = $res->fetch_assoc();
    $res_id_ok = $res_id['user_id'];

    $usr = $mysqli->query("SELECT * FROM `auth_user` WHERE `id` = '$res_id_ok'");
    $usr_fetch = $usr->fetch_assoc();
    $usr_username = $usr_fetch['username'];

    $filename = $_GET['img'];
    $path = __DIR__."/img/galeri/".$filename.".jpg";
    if(file_exists($path)){
        // Open the original image

        $image = new Imagick();
        $image->readImage(__DIR__."/img/galeri/$filename.jpg");

        $cropWidth = $image->getImageWidth();
        $cropHeight = $image->getImageHeight();
        /*
        // Open the watermark
        $watermark = new Imagick();
        $watermark->readImage(__DIR__."/img/watermark.png");

        // how big are the images?
        $iWidth = $image->getImageWidth();
        $iHeight = $image->getImageHeight();
        $wWidth = $watermark->getImageWidth();
        $wHeight = $watermark->getImageHeight();

        if ($iHeight < $wHeight || $iWidth < $wWidth) {
            // resize the watermark
            $watermark->scaleImage($iWidth, $iHeight);

            // get new size
            $wWidth = $watermark->getImageWidth();
            $wHeight = $watermark->getImageHeight();
        }

        // calculate the position
        $x = ($iWidth - $wWidth) / 2;
        $y = ($iHeight - $wHeight) / 2;

        $image->compositeImage($watermark, imagick::COMPOSITE_OVER, $x, $y);
        */
        $watermark = new Imagick();

        // Watermark text
        $text = $usr_username;

        // Create a new drawing palette
        $draw = new ImagickDraw();
        $watermark->newImage(340, 180, new ImagickPixel('none'));

        // Set font properties
        $draw->setFont('AndikaNewBasic-B.ttf');
        if($cropHeight > 4000){
            $draw->setFontSize(48);
        }elseif($cropHeight > 2000){
            $draw->setFontSize(28);
        }elseif($cropHeight > 1000){
            $draw->setFontSize(22);
        }else{
            $draw->setFontSize(20);
        }
        $draw->setFillColor('grey');
        $draw->setFillOpacity(.6);

        // Position text at the top left of the watermark
        $draw->setGravity(Imagick::GRAVITY_NORTHWEST);

        // Draw text on the watermark
        $watermark->annotateImage($draw, 30, 30, 0, $text);

        // Position text at the bottom right of the watermark
        $draw->setGravity(Imagick::GRAVITY_SOUTHEAST);

        // Draw text on the watermark
        $watermark->annotateImage($draw, 5, 15, 0, $text);

        // Repeatedly overlay watermark on image
        for ($w = 0; $w < $image->getImageWidth(); $w += 340) {
            for ($h = 0; $h < $image->getImageHeight(); $h += 180) {
                $image->compositeImage($watermark, Imagick::COMPOSITE_OVER, $w, $h);
            }
        }

        // Set output image format
        $image->setImageCompression(Imagick::COMPRESSION_JPEG);
        $image->setImageCompressionQuality(100);
        $image->setImageFormat($image->getImageFormat());
        header("Content-Type: image/" . $image->getImageFormat());
        echo $image;
    }else{
        echo 'notfound';
    }
    else:
    echo 'notfound';
    endif;
}