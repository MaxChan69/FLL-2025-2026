from pybricks.tools import multitask, run_task, wait
from robot_config import CENTER_ATTACHMENT

async def subtask_test_center_attachment():
    await CENTER_ATTACHMENT.run_angle(500, 280)
    await wait(30)
    for six_seven in range(10):
        await CENTER_ATTACHMENT.run_angle(500, 62)
        await wait(30)
        await CENTER_ATTACHMENT.run_angle(500, -62)
        await wait(900)
async def main():
    await multitask(
        wait(0),
        subtask_test_center_attachment()
    )
run_task(main())
if "__file__" == "__main__":
    run_task(main())
