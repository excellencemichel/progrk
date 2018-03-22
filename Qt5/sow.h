#ifndef SOW_H
#define SOW_H

#include <QWidget>

namespace Ui {
class sow;
}

class sow : public QWidget
{
    Q_OBJECT

public:
    explicit sow(QWidget *parent = 0);
    ~sow();

private:
    Ui::sow *ui;
};

#endif // SOW_H
