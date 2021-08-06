<?php
error_reporting(E_ALL);
ini_set('display_errors', 'On');
// Create objects
$image = new Imagick();
$image->readImage('img/nature_2.jpg');

$watermark = new Imagick();

// Watermark text
$text = 'Copyright';

// Create a new drawing palette
$draw = new ImagickDraw();
$watermark->newImage(140, 80, new ImagickPixel('none'));

// Set font properties
$draw->setFont('atomicage-regular.ttf');
$draw->setFillColor('grey');
$draw->setFillOpacity(.4);

// Position text at the top left of the watermark
$draw->setGravity(Imagick::GRAVITY_NORTHWEST);

// Draw text on the watermark
$watermark->annotateImage($draw, 10, 10, 0, $text);

// Position text at the bottom right of the watermark
$draw->setGravity(Imagick::GRAVITY_SOUTHEAST);

// Draw text on the watermark
$watermark->annotateImage($draw, 5, 15, 0, $text);

// Repeatedly overlay watermark on image
for ($w = 0; $w < $image->getImageWidth(); $w += 140) {
    for ($h = 0; $h < $image->getImageHeight(); $h += 80) {
        $image->compositeImage($watermark, Imagick::COMPOSITE_OVER, $w, $h);
    }
}

// Set output image format
$image->setImageFormat('png');

$image->setImageCompression(Imagick::COMPRESSION_JPEG);
$image->setImageCompressionQuality(10);
// Output the new image
header('Content-type: image/png');
echo $image;