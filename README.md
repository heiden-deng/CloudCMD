```
此乃迅达云命令行工具。

1.安装，配置
    下载本工具后，在终端命令行进入本项目目录，运行sudo python setup.py install命令进行安装。
    安装完成后，在home目录下会生成一个".speedycfg"文件, sudo vim .speedycfg编辑该文件，将access_key和secret_key填入对应位置。

2.命令有:censor, server, volume, cache, cdn, database, balancer, network, router, video，具体用法如下。
    1.censor:
        censor http://example.com/test.jpg, 鉴定图片http://example.com/test.jpg是否色情和暴恐
    2.server:
        server get_az, 获得所有可用数据中心
        server get_support_isps -az_name aaa, 获得数据中心aaa支持的网络运营商
        server get_os_images -az_name aaa, 获得数据中心aaa的操作系统镜像列表
        server list, 列出所有所有云主机
        server detail -id 1234, 显示id为1234的云主机的详细信息
        server backups -id 1234, 显示id为1234的云主机的备份列表
        server jobs -id 1234, 显示id为1234的云主机的任务列表
        server provison -available_zone aaa -isp bbb -image ccc -cpu 1 -memory 1024 -disk 20 -bandwidth 50, 创建云主机，其数据中心为aaa, 网络运营商为bbb, 操作系统镜像为ccc, cpu核数为1, 内存为1024M, 硬盘为20G, 带宽为50M
        server start -id 1234, 启动id为1234的云主机
        server restart -id 1234, 重启id为1234的云主机
        server stop -id 1234, 关闭id为1234的云主机
        server suspend -id 1234, 挂起id为1234的云主机
        server resume -id 1234, 恢复id为1234的云主机
        server backup -id 1234, -name aaa, 备份id为1234的云主机, 备份名为aaa
        server restore_backup -id 1234 -name aaa, 将id为1234的云主机从aaa备份中恢复
        server delete_backup -id 1234 -name aaa, 删除id为1234的云主机的名为aaa的备份
        server set_tag -id 1234 -tag aaa, 设置id为1234的云主机的标签为aaa
        server set_alias -id 1234 -alias aaa, 设置id为1234的云主机的别名为aaa
        server set_group -id 1234 -group aaa, 设置id为1234的云主机的分组为aaa
        server change_image -id 1234 -image_name aaa, 将id为1234的云主机的操作系统变更为aaa
        server attach_disk -id 1234 -volume_name aaa, 将名为aaa的云硬盘挂载到id为1234的云主机
        server detach_disk -id 1234 -volime_name aaa, 将名为aaa的云硬盘从id为1234的云主机卸载

    3.volume:
        volume list, 列出所有云硬盘
        volume detail -id 1234, 显示id为1234的云硬盘的详细信息
        volume provision -az aaa -size 20, 在aaa数据中心创建大小为20G的云硬盘
        volume snapshots -id 1234, 显示id为1234的云硬盘的快照列表
        volume jobs -id 1234, 显示id为1234的云硬盘的任务列表
        volumn set_tag -id 1234 -tag aaa, 将id为1234的云硬盘的标签设置为aaa
        volume set_alias -id 1234 -alias aaa, 将id为1234的云硬盘的别名设置为aaa
        volume set_group -id 1234 -group aaa, 将id为1234的云硬盘的分组设置为aaa
        volume create_snapshot -id 1234 -snapshot aaa, 为id为1234的云硬盘创建快照
        volume rollback_snapshot -id 1234 -snapshot aaa, 将id为1234的云硬盘的aaa快照回滚
        volume delete_snapshot -id 1234 -snapshot aaa, 将id为1234的云硬盘的名为aaa的快照删除
        volume get_az, 获得所有可用数据中心

    4.cdn:
        cdn list, 列出所有域名
        cdn detail -id 1234, 显示cdn详细信息
        cdn modify -id 1234 -domain abc.com -origin_ip 0.0.0.0 -cache_type aaa, 将id为1234cdn的域名改为domain, 源站ip改为0.0.0.0, 缓存策略改为cache_type
        cdn pause -id 1234, 暂停id为1234的cdn
        cdn resume -id 1234, 恢复id为1234的cdn
        cdn logs -id 1234 -start_date 2015-1-1 -end_date 2016-1-1, 列出2015-1-1到2016-1-1时间内的所有日志
        cdn refresh_list, 刷新纪录列表
        cdn add_refresh -refresh_type aaa -urls [url1, url2, url3], 将url1, url2, url3添加到url刷新, 刷新类型为aaa
        cdn redo_refresh -id 1234, 重新刷新id为1234的刷新文件目录
        cdn delete_refresh -ids [1, 2, 3], 将id为1, 2, 3的刷新纪录删除
        cdn preload_list, 预加载纪录列表
        cdn add_preload -urls [url1, url2, url3], 将url1, url2, url3添加到预加载
        cdn delete_preload -ids [1, 2, 3], 删除id为1, 2, 3的预加载纪录
        cdn set_group -id 1234 -group aaa, 设置id的1234的cdn分组为aaa
        cdn get_bandwidth -ids [1, 2, 3], 获得id为1, 2, 3的cdn的带宽记录

    5.balancer:
        balancer get_az, 获得可用数据中心
        balancer get_support_isps -az aaa, 获得数据中心aaa支持的网络运营商
        balancer list, 列出所有负载均衡
        balancer create_load_balancer -az aaa -isp bbb -bandwidth 50, 在aaa数据中创建网络运营商为bbb,带宽为50M的负载均衡
        balancer add_backend_cloud_server -lbid 1234 -csid 5678 -weight 5 -ip 1.1.1.1, 为lbid为1234的负载均衡添加csid为5678, 权重为5, ip为1.1.1.1的后端云主机
        balancer add_backend_database -lbid 1234 -did 5678 -weight 5 -ip 1.1.1.1, 为lbid为1234的负载均衡添加did为5678, 权重为5, ip为1.1.1.1的后端数据库
        balancer ad_backend_cache -lbid 1234 -cid 5678 -weight 5 -ip 1.1.1.1, 为lbid为1234的负载均衡添加cid为5678, 权重为5, ip为1.1.1.1的后端缓存
        balancer update_backend -lbid 1234 -bid 5678 -weight 5 -ip 1.1.1.1, 将lbid为1234的负载均衡的bid为5678的后端的权重更新为5, ip更新为1.1.1.1
        balancer delete_backend -lbid 1234 -bid 5678, 将lbid为1234的负载均衡的bid为5678的后端删除
        balancer add_app -lbid 1234 -frontend 81 -backend 82 -protocol aaa -strategy bbb -check_interval 5 -rise_times 10 -fall_times 10, 向lbid为1234的负载均衡添加应用, 其前端端口为81, 后端端口为82, 协议为aaa, 负载均衡策略为bbb, 健康检查间隔为5秒, 下线监测阀值为10, 在线监测阀值为10
        balancer detail -lbid 1234, lbid为1234的负载均衡的详细信息
        balancer update_app -lbid 1234 -appid 5678 -frontend 90 -backend 91 -protocol aaa -strategy bbb -check_interval 6 -rise_times 11 -fall_times 11, 更新lbid为1234的负载均衡的appid为5678的应用, 将其前端端口改为90, 后端端口改为91, 协议改为aaa, 负载均衡策略改为bbb, 健康检查间隔改为6秒, 下线监测阀值改为11, 在线监测阀值改为11
        balancer delete_app -lbid 1234 -appid 5678, 删除lbid为1234的负载均衡的appid为5678的应用

    6.network
        network list, 网络列表
        network detail -id 1234, id为1234的网络的详细信息
        network create -az aaa, 在数据中心aaa创建网络
        network delete -id 1234, 删除id为1234网络
        network set_alias -id 1234 -alias aaa, 将id为1234的网络别名设置为aaa
        network set_group -id 1234 -group aaa, 将id为1234的网络分组设置为aaa
        network groups, 网路分组列表

    7.database
        database create_database -az aaa -isp bbb -image ccc -memory 1024 -disk 20 -bandwidth 50, 在数据中心aaa创建数据库镜像为ccc, 内存为1024M, 硬盘容量为20, 带宽为50M的数据库, 其网络运营商为bbb
        database list, 列出所有数据库
        database get_az, 获得可用数据中心
        database get_support_isps -az aaa, 获得数据中心aaa支持的网络运营商
        database get_images, 获得数据库镜像

    8.cache
        cache create_cache -az aaa -isp bbb -image ccc -memory 1024 -disk 20 -bandwidth 50, 在数据中心aaa创建数据库镜像为ccc, 内存为1024M, 硬盘容量为20, 带宽为50M的缓存, 其网络运营商为bbb
        cache list, 列出所有数据库
        cache get_az, 获得可用数据中心
        cache get_support_isps -az aaa, 获得数据中心aaa支持的网络运营商
        cache get_images, 获得缓存数据库镜像

    9.router
        router list, 路由器列表
        router detail -id 1234, id为1234的路由器的详细信息
        router create_nat_role -id 1234 -port 88 -protocol aaa -target_ip 1.1.1.1 -target_port 89, 为id为1234的路由器创建nat规则, nat端口号为88, nat协议为aaa, 目标ip为1.1.1.1, 目标端口号为89
        router edit_nat_role -id 1234 -port 88 -protocol aaa -target_ip 1.1.1.1 -target_port 89, 为id为1234的路由器更新nat规则, 跟新后的nat端口号为88, nat协议为aaa, 目标ip为1.1.1.1, 目标端口号为89
        router delete_nat_role -id 1234 -port 88 -protocol aaa, 删除id为1234的路由器的nat端口号为88, nat协议为aaa的nat规则
        router set_group -id 1234 -group aaa, 设置id为1234的路由器分组为aaa
        router groups, 列出所有路由器分组
        router set_alias -id 1234 -alias aaa, 设置id为1234的路由器别名为aaa
        router stop -id 1234, 停止id为1234的路由器
        router start -id 1234, 开启id为1234的路由器
        router jobs -id 1234, id为1234的路由器任务列表
        router support_features -id, id为1234的路由器支持的特性
        router join -id 1234 -network aaa -ip 1.1.1.1 -mask 255.255.255.0, 将id为1234的路由器加入网络名为aaa私有网络, 其在私有网络中的ip为1.1.1.1, 网关为255.255.255.0
        router toggle_private_network -id 1234, id为1234的路由器的默认内网开关
        router reload -id 1234, 重新加载id为1234的路由器
        router rejoin -id 1234 -network aaa -ip 1.1.1.1 -mask 255.255.255.0, 将id为1234的路由器重新加入网络名为aaa私有网络, 其在私有网络中的ip为1.1.1.1, 网关为255.255.255.0
        router leave -id 1234 -network aaa, id为1234的路由器离开aaa网络

    10.video
        video create_vod -name aaa -uploaded_video_file bbb, 创建vod视频, 其名字为aaa, 对应的已上传视频文件id为bbb
        video vods, 点播视频列表
        video detail -id 1234, id为1234的vod视频详细信息
        video modify_vod -id 1234 -name aaa -labels bbb -introduction ccc -origin_image_file ddd, 修改id为1234的vod视频信息, 修改后其名字为aaa, 标签为bbb, 简介为ccc, 缩略图id为ddd
```
