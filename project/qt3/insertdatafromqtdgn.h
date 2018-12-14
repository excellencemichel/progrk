#ifndef INSERTDATAFROMDTDGN_H
#define INSERTDATAFROMDTDGN_H

#include <QMainWindow>

namespace Ui {
class insertDataFromDtDgn;
}

class insertDataFromDtDgn : public QMainWindow
{
    Q_OBJECT

public:
    explicit insertDataFromDtDgn(QWidget *parent = 0);
    ~insertDataFromDtDgn();

private:
    Ui::insertDataFromDtDgn *ui;
};

#endif // INSERTDATAFROMDTDGN_H
