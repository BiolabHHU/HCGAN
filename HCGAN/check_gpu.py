import torch


def check_gpu_availability():
    """检查当前系统的GPU支持情况"""
    print("=" * 50)
    print("GPU/CUDA可用性检测报告")
    print("=" * 50)

    # 基础检测
    cuda_available = torch.cuda.is_available()
    print(f"[1] CUDA是否可用: {'可用' if cuda_available else '不可用'}")

    if not cuda_available:
        print("\n未检测到可用GPU，将使用CPU进行训练")
        return

    # 详细设备信息
    device_count = torch.cuda.device_count()
    current_device = torch.cuda.current_device()
    device_name = torch.cuda.get_device_name(current_device)
    device_capability = torch.cuda.get_device_capability(current_device)

    print(f"\n检测到{device_count}个GPU设备:")
    print(f"当前使用设备: {current_device} ({device_name})")
    print(f"Compute Capability: {device_capability[0]}.{device_capability[1]}")

    # 显存信息
    total_mem = torch.cuda.get_device_properties(current_device).total_memory / 1024 ** 3
    allocated_mem = torch.cuda.memory_allocated(current_device) / 1024 ** 3
    cached_mem = torch.cuda.memory_reserved(current_device) / 1024 ** 3

    print(f"\n显存使用情况:")
    print(f"总显存: {total_mem:.2f} GB")
    print(f"已分配显存: {allocated_mem:.2f} GB")
    print(f"缓存显存: {cached_mem:.2f} GB")

    # 推荐设置
    print("\n推荐配置:")
    print(f"建议设置: device = torch.device('cuda:{current_device}')")
    print("典型用法示例:")
    print(">> model = MyModel().to(device)")
    print(">> data = data.to(device)")


if __name__ == "__main__":
    check_gpu_availability()