#ifndef CALCULATRICE_H
#define CALCULATRICE_H

#include <QWidget>

namespace Ui {
class calculatrice;
}

class calculatrice : public QWidget
{
    Q_OBJECT

public:
    explicit calculatrice(QWidget *parent = 0);
    ~calculatrice();

private:
    Ui::calculatrice *ui;
};

#endif // CALCULATRICE_H
