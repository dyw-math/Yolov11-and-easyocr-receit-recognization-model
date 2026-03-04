import yaml
import os

dataset_path = os.path.join(HOME, "datasets", "receit-tel-date-total-2")
data_yaml_path = os.path.join(dataset_path, "data.yaml")

# 读取 data.yaml 文件
with open(data_yaml_path, 'r') as f:
    data_config = yaml.safe_load(f)

# 更新 'path' 字段为绝对路径
data_config['path'] = dataset_path

# 将更新后的配置写回 data.yaml 文件
with open(data_yaml_path, 'w') as f:
    yaml.safe_dump(data_config, f)

print(f"Updated {data_yaml_path} with path: {data_config['path']}")

# 再次打印 data.yaml 文件内容以验证修改
print("\n--- Updated data.yaml content ---")
!cat {data_yaml_path}
