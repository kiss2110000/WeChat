import time


def openWXFS(d):
    """启用微信分身"""
    udid = d.device_info["udid"]
    num = 0
    while num < 5:
        try:
            if udid == "c176b27d-18:e2:9f:2e:dd:78-vivo_X23Plus":
                """vivo X23"""
                d.shell("am start com.tencent.mm/com.tencent.mm.ui.LauncherUI")
                d(text="Ⅱ·微信").click(timeout=0.5)
                print(" -- 点击了微信分身")
            elif udid == "c176b27d-18:e2:9f:2e:dd:78-vivo_X7Plus":
                """vivo X7"""
                # Home键返回桌面,点击微信分身
                d.shell("input keyevent 3")
                d(text=u"Ⅱ·微信", resourceId="com.bbk.launcher2:id/item_title").click(timeout=5)
            num = 6
        except:
            num += 1
            time.sleep(1)
            print("警告：正在尝试重新打开微信分身！")


def openWXBZ(d):
    # 启动微信本尊,打开朋友发表页面
    udid = d.device_info["udid"]
    num = 0
    while num < 5:
        try:
            if udid == "c176b27d-18:e2:9f:2e:dd:78-vivo_X23Plus":
                d.shell("am start com.tencent.mm/com.tencent.mm.ui.LauncherUI")
                d(text="微信").click(timeout=0.5)
            elif udid == "c176b27d-18:e2:9f:2e:dd:78-vivo_X7Plus":
                d.shell("am start com.tencent.mm/com.tencent.mm.ui.LauncherUI")
            num = 6
        except:
            num += 1
            time.sleep(1)
            print("警告：正在尝试重新打开微信本尊！")


def openDownloadWXXC(d):
    openWXFS(d)


def openUploadWXPYQ(d):
    openWXBZ(d)
    # 检查是否为发表页面
    result = d(description="拍照分享").exists(timeout=1.5)
    if not result:
        is_gone = d(description="返回",
                    packageName="com.tencent.mm",
                    className="android.widget.ImageView").click_gone(maxretry=20, interval=0.01)
        if is_gone is True:
            d(text="发现").click(timeout=5)
            d(text="朋友圈").click(timeout=5)
            print(" -- 已打开朋友圈页面")
            return True
        print("错误：找不到朋友圈页面！")
        return False
    return True


if __name__=='__main__':
    import uiautomator2 as u2
    d = u2.connect()
    openDownloadWXXC()
