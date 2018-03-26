#ifndef MISEPAGE_H
#define MISEPAGE_H

#include <QMainWindow>

namespace Ui {
class MisePage;
}

class MisePage : public QMainWindow
{
    Q_OBJECT

public:
    explicit MisePage(QWidget *parent = 0);
    ~MisePage();

private:
    Ui::MisePage *ui;
};

#endif // MISEPAGE_H
