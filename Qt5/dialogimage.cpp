#include "dialogimage.h"
#include "ui_dialogimage.h"

DialogImage::DialogImage(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogImage)
{
    ui->setupUi(this);
}

DialogImage::~DialogImage()
{
    delete ui;
}
