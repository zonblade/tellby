<?php

function imgprint_watermark($1,$2,$3){
    $image = new Imagick();
    $image->readImage($1);

    // Open the watermark
    $watermark = new Imagick();
    $watermark->readImage($2);

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

    $image->setImageCompression(Imagick::FILTER_LANCZOS);
    $image->setImageCompressionQuality($3);
    header("Content-Type: image/" . $image->getImageFormat());
    echo $image;
}

function imgprint_pure($1,$2){
    $image = new Imagick();
    $image->readImage($1);
    $image->setImageCompression(Imagick::FILTER_LANCZOS);
    $image->setImageCompressionQuality($2);
    header("Content-Type: image/" . $image->getImageFormat());
    echo $image;
}