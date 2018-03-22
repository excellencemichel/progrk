#ifndef DATALISTE_H
#define DATALISTE_H

#include <QMainWindow>

namespace Ui {
class Dataliste;
}

class Dataliste : public QMainWindow
{
    Q_OBJECT

public:
    explicit Dataliste(QWidget *parent = 0);
    ~Dataliste();

private:
    Ui::Dataliste *ui;
};

#endif // DATALISTE_H
