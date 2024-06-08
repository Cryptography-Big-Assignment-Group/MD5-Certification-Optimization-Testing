"""
可视化界面：运行即可
"""

import tkinter as tk
import user_select


def generate_dialog():
    def execute_function():
        # 获取用户选择
        selected_options = []
        if option1_var.get():
            selected_options.append("Option 1")
        if option2_var.get():
            selected_options.append("Option 2")
        if option3_var.get():
            selected_options.append("Option 3")
        if option4_var.get():
            selected_options.append("Option 4")

        # 执行函数并在输出框内显示结果
        result = your_function(dialog_entry.get("1.0", tk.END).strip(), selected_options)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    def your_function(input_text, selected_options):
        # 在这里编写你的函数逻辑
        # 根据输入文本和选择的选项，进行相应的处理
        # 返回处理结果
        text_md5 = user_select.MD5_select(input_text, selected_options)
        # 这里只是一个示例
        result = "输入消息: {}\n".format(input_text)
        result += "选择的选项: {}\n".format(", ".join(selected_options))
        result = result + "函数处理后的消息摘要:" + text_md5
        return result

    # 创建主窗口
    window = tk.Tk()
    window.title("MD5优化选择器")

    # 对话框标签和输入框
    dialog_label = tk.Label(window, text="请输入消息文本(英文/数字/符号均可):")
    dialog_label.pack()

    dialog_frame = tk.Frame(window)
    dialog_frame.pack()

    dialog_entry = tk.Text(dialog_frame, height=8, width=40)
    dialog_entry.pack()

    # 选项复选框
    option1_var = tk.IntVar()
    option1_checkbox = tk.Checkbutton(window, text="1.对填充后消息分组计算立方和\t", variable=option1_var)
    option1_checkbox.pack()

    option2_var = tk.IntVar()
    option2_checkbox = tk.Checkbutton(window, text="2.使用混沌logistic映射代换表\t", variable=option2_var)
    option2_checkbox.pack()

    option3_var = tk.IntVar()
    option3_checkbox = tk.Checkbutton(window, text="3.使用Henon纵向模乘法\t", variable=option3_var)
    option3_checkbox.pack()

    option4_var = tk.IntVar()
    option4_checkbox = tk.Checkbutton(window, text="4.对结果使用S盒子代换\t", variable=option4_var)
    option4_checkbox.pack()

    # 执行按钮
    execute_button = tk.Button(window, text="输出消息摘要", command=execute_function)
    execute_button.pack()

    # 输出文本框
    output_text = tk.Text(window, height=10, width=60)
    output_text.pack()

    window.mainloop()


# 调用函数启动可视化界面
generate_dialog()
