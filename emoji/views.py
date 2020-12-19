from django.shortcuts import render


def emoji(request):
    activity = [
       u'\U000026bd'+ u'\U0000fe0f', u'\U0001f3c0', u'\U0001f3c8', u'\U000026be'+ u'\U0000fe0f', u'\U0001f94e', u'\U0001f3be', u'\U0001f3d0', u'\U0001f3c9', u'\U0001f94f', u'\U0001f3b1', u'\U0001fa80', u'\U0001f3d3', u'\U0001f3f8', u'\U0001f3d2', u'\U0001f3d1', u'\U0001f94d', u'\U0001f3cf', u'\U0001fa83', u'\U0001f945', u'\U000026f3'+ u'\U0000fe0f', u'\U0001fa81', u'\U0001f3f9', u'\U0001f3a3', u'\U0001f93f', u'\U0001f94a', u'\U0001f94b', u'\U0001f3bd', u'\U0001f6f9', u'\U0001f6fc', u'\U0001f6f7', u'\U000026f8', u'\U0001f94c', u'\U0001f3bf', u'\U000026f7', u'\U0001f3c2', u'\U0001fa82', u'\U0001f3cb'+ u'\U0000fe0f'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f3cb'+ u'\U0000fe0f', u'\U0001f3cb'+ u'\U0000fe0f'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f93c'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f93c', u'\U0001f93c'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f938'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f938', u'\U0001f938'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U000026f9'+ u'\U0000fe0f'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U000026f9'+ u'\U0000fe0f', u'\U000026f9'+ u'\U0000fe0f'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f93a', u'\U0001f93e'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f93e', u'\U0001f93e'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f3cc'+ u'\U0000fe0f'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f3cc'+ u'\U0000fe0f', u'\U0001f3cc'+ u'\U0000fe0f'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f3c7', u'\U0001f9d8'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f9d8', u'\U0001f9d8'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f3c4'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f3c4', u'\U0001f3c4'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f3ca'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f3ca', u'\U0001f3ca'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f93d'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f93d', u'\U0001f93d'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f6a3'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f6a3', u'\U0001f6a3'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f9d7'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f9d7', u'\U0001f9d7'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f6b5'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f6b5', u'\U0001f6b5'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f6b4'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f6b4', u'\U0001f6b4'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f3c6', u'\U0001f947', u'\U0001f948', u'\U0001f949', u'\U0001f3c5', u'\U0001f396', u'\U0001f3f5', u'\U0001f397', u'\U0001f3ab', u'\U0001f39f', u'\U0001f3aa', u'\U0001f939', u'\U0001f939'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f939'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f3ad', u'\U0001fa70', u'\U0001f3a8', u'\U0001f3ac', u'\U0001f3a4', u'\U0001f3a7', u'\U0001f3bc', u'\U0001f3b9', u'\U0001f941', u'\U0001fa98', u'\U0001f3b7', u'\U0001f3ba', u'\U0001fa97', u'\U0001f3b8', u'\U0001fa95', u'\U0001f3bb', u'\U0001f3b2', u'\U0000265f', u'\U0001f3af', u'\U0001f3b3', u'\U0001f3ae', u'\U0001f3b0', u'\U0001f9e9'
    ]
    food = [
        u'\U0001f34f', u'\U0001f34e', u'\U0001f350', u'\U0001f34a', u'\U0001f34b', u'\U0001f34c', u'\U0001f349', u'\U0001f347', u'\U0001f353', u'\U0001fad0', u'\U0001f348', u'\U0001f352', u'\U0001f351', u'\U0001f96d', u'\U0001f34d', u'\U0001f965', u'\U0001f95d', u'\U0001f345', u'\U0001f346', u'\U0001f951', u'\U0001f966', u'\U0001f96c', u'\U0001f952', u'\U0001f336', u'\U0001fad1', u'\U0001f33d', u'\U0001f955', u'\U0001fad2', u'\U0001f9c4', u'\U0001f9c5', u'\U0001f954', u'\U0001f360', u'\U0001f950', u'\U0001f96f', u'\U0001f35e', u'\U0001f956', u'\U0001f968', u'\U0001f9c0', u'\U0001f95a', u'\U0001f373', u'\U0001f9c8', u'\U0001f95e', u'\U0001f9c7', u'\U0001f953', u'\U0001f969', u'\U0001f357', u'\U0001f356', u'\U0001f9b4', u'\U0001f32d', u'\U0001f354', u'\U0001f35f', u'\U0001f355', u'\U0001fad3', u'\U0001f96a', u'\U0001f959', u'\U0001f9c6', u'\U0001f32e', u'\U0001f32f', u'\U0001fad4', u'\U0001f957', u'\U0001f958', u'\U0001fad5', u'\U0001f96b', u'\U0001f35d', u'\U0001f35c', u'\U0001f372', u'\U0001f35b', u'\U0001f363', u'\U0001f371', u'\U0001f95f', u'\U0001f9aa', u'\U0001f364', u'\U0001f359', u'\U0001f35a', u'\U0001f358', u'\U0001f365', u'\U0001f960', u'\U0001f96e', u'\U0001f362', u'\U0001f361', u'\U0001f367', u'\U0001f368', u'\U0001f366', u'\U0001f967', u'\U0001f9c1', u'\U0001f370', u'\U0001f382', u'\U0001f36e', u'\U0001f36d', u'\U0001f36c', u'\U0001f36b', u'\U0001f37f', u'\U0001f369', u'\U0001f36a', u'\U0001f330', u'\U0001f95c', u'\U0001f36f', u'\U0001f95b', u'\U0001f37c', u'\U0001fad6', u'\U00002615'+ u'\U0000fe0f', u'\U0001f375', u'\U0001f9c3', u'\U0001f964', u'\U0001f9cb', u'\U0001f376', u'\U0001f37a', u'\U0001f37b', u'\U0001f942', u'\U0001f377', u'\U0001f943', u'\U0001f378', u'\U0001f379', u'\U0001f9c9', u'\U0001f37e', u'\U0001f9ca', u'\U0001f944', u'\U0001f374', u'\U0001f37d', u'\U0001f963', u'\U0001f961', u'\U0001f962', u'\U0001f9c2',
    ]
    nature = [
        u'\U0001f436', u'\U0001f431', u'\U0001f42d', u'\U0001f439', u'\U0001f430', u'\U0001f98a', u'\U0001f43b', u'\U0001f43c', u'\U0001f43b'+ u'\U0000200d'+ u'\U00002744'+ u'\U0000fe0f', u'\U0001f428', u'\U0001f42f', u'\U0001f981', u'\U0001f42e', u'\U0001f437', u'\U0001f43d', u'\U0001f438', u'\U0001f435', u'\U0001f648', u'\U0001f649', u'\U0001f64a', u'\U0001f412', u'\U0001f414', u'\U0001f427', u'\U0001f426', u'\U0001f424', u'\U0001f423', u'\U0001f425', u'\U0001f986', u'\U0001f985', u'\U0001f989', u'\U0001f987', u'\U0001f43a', u'\U0001f417', u'\U0001f434', u'\U0001f984', u'\U0001f41d', u'\U0001fab1', u'\U0001f41b', u'\U0001f98b', u'\U0001f40c', u'\U0001f41e', u'\U0001f41c', u'\U0001fab0', u'\U0001fab2', u'\U0001fab3', u'\U0001f99f', u'\U0001f997', u'\U0001f577', u'\U0001f578', u'\U0001f982', u'\U0001f422', u'\U0001f40d', u'\U0001f98e', u'\U0001f996', u'\U0001f995', u'\U0001f419', u'\U0001f991', u'\U0001f990', u'\U0001f99e', u'\U0001f980', u'\U0001f421', u'\U0001f420', u'\U0001f41f', u'\U0001f42c', u'\U0001f433', u'\U0001f40b', u'\U0001f988', u'\U0001f40a', u'\U0001f405', u'\U0001f406', u'\U0001f993', u'\U0001f98d', u'\U0001f9a7', u'\U0001f9a3', u'\U0001f418', u'\U0001f99b', u'\U0001f98f', u'\U0001f42a', u'\U0001f42b', u'\U0001f992', u'\U0001f998', u'\U0001f9ac', u'\U0001f403', u'\U0001f402', u'\U0001f404', u'\U0001f40e', u'\U0001f416', u'\U0001f40f', u'\U0001f411', u'\U0001f999', u'\U0001f410', u'\U0001f98c', u'\U0001f415', u'\U0001f429', u'\U0001f9ae', u'\U0001f415'+ u'\U0000200d'+ u'\U0001f9ba', u'\U0001f408', u'\U0001f408'+ u'\U0000200d'+ u'\U00002b1b', u'\U0001fab6', u'\U0001f413', u'\U0001f983', u'\U0001f9a4', u'\U0001f99a', u'\U0001f99c', u'\U0001f9a2', u'\U0001f9a9', u'\U0001f54a', u'\U0001f407', u'\U0001f99d', u'\U0001f9a8', u'\U0001f9a1', u'\U0001f9ab', u'\U0001f9a6', u'\U0001f9a5', u'\U0001f401', u'\U0001f400', u'\U0001f43f', u'\U0001f994', u'\U0001f43e', u'\U0001f409', u'\U0001f432', u'\U0001f335', u'\U0001f384', u'\U0001f332', u'\U0001f333', u'\U0001f334', u'\U0001fab5', u'\U0001f331', u'\U0001f33f', u'\U00002618'+ u'\U0000fe0f', u'\U0001f340', u'\U0001f38d', u'\U0001fab4', u'\U0001f38b', u'\U0001f343', u'\U0001f342', u'\U0001f341', u'\U0001f344', u'\U0001f41a', u'\U0001faa8', u'\U0001f33e', u'\U0001f490', u'\U0001f337', u'\U0001f339', u'\U0001f940', u'\U0001f33a', u'\U0001f338', u'\U0001f33c', u'\U0001f33b', u'\U0001f31e', u'\U0001f31d', u'\U0001f31b', u'\U0001f31c', u'\U0001f31a', u'\U0001f315', u'\U0001f316', u'\U0001f317', u'\U0001f318', u'\U0001f311', u'\U0001f312', u'\U0001f313', u'\U0001f314', u'\U0001f319', u'\U0001f30e', u'\U0001f30d', u'\U0001f30f', u'\U0001fa90', u'\U0001f4ab', u'\U00002b50'+ u'\U0000fe0f', u'\U0001f31f', u'\U00002728', u'\U000026a1'+ u'\U0000fe0f', u'\U00002604'+ u'\U0000fe0f', u'\U0001f4a5', u'\U0001f525', u'\U0001f32a', u'\U0001f308', u'\U00002600'+ u'\U0000fe0f', u'\U0001f324', u'\U000026c5'+ u'\U0000fe0f', u'\U0001f325', u'\U00002601'+ u'\U0000fe0f', u'\U0001f326', u'\U0001f327', u'\U000026c8', u'\U0001f329', u'\U0001f328', u'\U00002744'+ u'\U0000fe0f', u'\U00002603'+ u'\U0000fe0f', u'\U000026c4'+ u'\U0000fe0f', u'\U0001f32c', u'\U0001f4a8', u'\U0001f4a7', u'\U0001f4a6', u'\U00002614'+ u'\U0000fe0f', u'\U00002602'+ u'\U0000fe0f', u'\U0001f30a', u'\U0001f32b',
    ]
    christmas = [
        u'\U0001f476', u'\U0001f47c', u'\U0001f385', u'\U0001f936', 
        u'\U0001f46a', u'\U0001f98c', u'\U0001f36a', u'\U0001f95b',
        u'\U0001f377', u'\U0001f374', u'\U000026ea', u'\U0001f31f',
        u'\U000026c4', u'\U0001f525', u'\U0001f384', u'\U0001f381',
        u'\U0001f9e6', u'\U0001f514', u'\U00002744'+ u'\U0000fe0f', 
        u'\U0001f56f'+ u'\U0000fe0f', u'\U0000271d'+ u'\U0000fe0f',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f384', u'\U0001f6d0',
        u'\U00002603'+ u'\U0000fe0f'
    ]
    faces = [
        u'\U0001f600', u'\U0001f601', u'\U0001f602', u'\U0001f603',
        u'\U0001f604', u'\U0001f605', u'\U0001f606', u'\U0001f923', 
        u'\U0001f60A', u'\U0001f607', u'\U0001f972', u'\U0001f642',
        u'\U0000263a', u'\U0001f643', u'\U0001f609', u'\U0001f60c',
        u'\U0001f60d', u'\U0001f970', u'\U0001f618', u'\U0001f617',
        u'\U0001f619', u'\U0001f61a', u'\U0001f60b', u'\U0001f61b',
        u'\U0001f61d', u'\U0001f61c', u'\U0001f92a', u'\U0001f928',
        u'\U0001f9d0', u'\U0001f913', u'\U0001f60e', u'\U0001f978',
        u'\U0001f929', u'\U0001f973', u'\U0001f60f', u'\U0001f612',
        u'\U0001f61e', u'\U0001f614', u'\U0001f61f', u'\U0001f615',
        u'\U0001f641', u'\U00002639', u'\U0000fe0f', u'\U0001f623',
        u'\U0001f616', u'\U0001f62b', u'\U0001f629', u'\U0001f97a',
        u'\U0001f622', u'\U0001f62d', u'\U0001f624', u'\U0001f620',
        u'\U0001f621', u'\U0001f92c', u'\U0001f92f', u'\U0001f633',
        u'\U0001f975', u'\U0001f976', u'\U0001f631', u'\U0001f628',
        u'\U0001f630', u'\U0001f625', u'\U0001f613', u'\U0001f917',
        u'\U0001f914', u'\U0001f92d', u'\U0001f92b', u'\U0001f925',
        u'\U0001f636', u'\U0001f610', u'\U0001f611', u'\U0001f62c',
        u'\U0001f644', u'\U0001f62f', u'\U0001f626', u'\U0001f627',
        u'\U0001f62e', u'\U0001f632', u'\U0001f971', u'\U0001f634',
        u'\U0001f924', u'\U0001f62a', u'\U0001f635', u'\U0001f910',
        u'\U0001f974', u'\U0001f922', u'\U0001f92e', u'\U0001f927',
        u'\U0001f637', u'\U0001f912', u'\U0001f915', u'\U0001f911',
        u'\U0001f920', u'\U0001f608', u'\U0001f47f', u'\U0001f479',
        u'\U0001f47a', u'\U0001f921', u'\U0001f4a9', u'\U0001f47b',
        u'\U0001f480', u'\U00002620', u'\U0000fe0f', u'\U0001f47d',
        u'\U0001f47e', u'\U0001f916', u'\U0001f383', u'\U0001f63a',
        u'\U0001f638', u'\U0001f639', u'\U0001f63b', u'\U0001f63c',
        u'\U0001f63d', u'\U0001f640', u'\U0001f63f', u'\U0001f63e'
    ]
    gestures =  [
        u'\U0001f44b', u'\U0001f91a', u'\U0001f590', u'\U0000270b',
        u'\U0001f596', u'\U0001f44c', u'\U0001f90c', u'\U0001f90f',
        u'\U0001f91e', u'\U0001f91f', u'\U0001f918', u'\U0001f919',
        u'\U0001f448', u'\U0001f449', u'\U0001f446', u'\U0001f595',
        u'\U0001f447', u'\U0001f44d', u'\U0001f44e', u'\U0000270a',
        u'\U0001f44a', u'\U0001f91b', u'\U0001f91c', u'\U0001f44f',
        u'\U0001f64c', u'\U0001f450', u'\U0001f932', u'\U0001f91d',
        u'\U0001f64f', u'\U0001f485', u'\U0001f933', u'\U0001f4aa',
        u'\U0001f9be', u'\U0001f9b5', u'\U0001f9bf', u'\U0001f9b6',
        u'\U0001f463', u'\U0001f442', u'\U0001f9bb', u'\U0001f443',
        u'\U0001fac0', u'\U0001fac1', u'\U0001f9e0', u'\U0001f9b7',
        u'\U0001f9b4', u'\U0001f440', u'\U0001f441', u'\U0001f445',
        u'\U0001f444', u'\U0001f48b', u'\U0000270c'+ u'\U0000fe0f', 
        u'\U0000261d'+ u'\U0000fe0f', u'\U0000270d'+ u'\U0000fe0f',
        u'\U0001fa78', 
    ]
    people = [
        u'\U0001f476', u'\U0001f467', u'\U0001f9d2', u'\U0001f466',
        u'\U0001f469', u'\U0001f9d1', u'\U0001f468', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f9b1',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f9b1', u'\U0001f468'+ u'\U0000200d'+ u'\U0001f9b1',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f9b0', u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f9b0',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f9b0',
        u'\U0001f471'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f',
        u'\U0001f471', u'\U0001f471'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f9b3', u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f9b3',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f9b3', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f9b2',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f9b2', u'\U0001f468'+ u'\U0000200d'+ u'\U0001f9b2',
        u'\U0001f9d4', u'\U0001f475', u'\U0001f9d3', u'\U0001f474', u'\U0001f472',
        u'\U0001f473'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f473',
        u'\U0001f473'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f9d5',
        u'\U0001f46e'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f46e',
        u'\U0001f46e'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f477'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f477',
        u'\U0001f477'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f482'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f482',
        u'\U0001f482'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f575'+ u'\U0000fe0f'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f',
        u'\U0001f575'+ u'\U0000fe0f', u'\U0001f575'+ u'\U0000fe0f'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f469'+ u'\U0000200d'+ u'\U00002695'+ u'\U0000fe0f',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U00002695'+ u'\U0000fe0f',
        u'\U0001f468'+ u'\U0000200d'+ u'\U00002695'+ u'\U0000fe0f',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f33e', u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f33e',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f33e', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f373',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f373', u'\U0001f468'+ u'\U0000200d'+ u'\U0001f373',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f393', u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f393',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f393', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f3a4',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f3a4', u'\U0001f468'+ u'\U0000200d'+ u'\U0001f3a4',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f3eb', u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f3eb',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f3eb', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f3ed',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f3ed', u'\U0001f468'+ u'\U0000200d'+ u'\U0001f3ed',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f4bb', u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f4bb',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f4bb', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f4bc',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f4bc', u'\U0001f468'+ u'\U0000200d'+ u'\U0001f4bc',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f527', u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f527',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f527', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f52c',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f52c', u'\U0001f468'+ u'\U0000200d'+ u'\U0001f52c',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f3a8', u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f3a8',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f3a8', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f692',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f692', u'\U0001f468'+ u'\U0000200d'+ u'\U0001f692',
        u'\U0001f469'+ u'\U0000200d'+ u'\U00002708'+ u'\U0000fe0f',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U00002708'+ u'\U0000fe0f',
        u'\U0001f468'+ u'\U0000200d'+ u'\U00002708'+ u'\U0000fe0f',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f680', u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f680',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f680',
        u'\U0001f469'+ u'\U0000200d'+ u'\U00002696'+ u'\U0000fe0f',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U00002696'+ u'\U0000fe0f',
        u'\U0001f468'+ u'\U0000200d'+ u'\U00002696'+ u'\U0000fe0f',
        u'\U0001f470'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f',
        u'\U0001f470', u'\U0001f470'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f935'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f935',
        u'\U0001f935'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f478',
        u'\U0001f934', u'\U0001f977', u'\U0001f9b8'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f',
        u'\U0001f9b8', u'\U0001f9b8'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f9b9'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f9b9',
        u'\U0001f9b9'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f936',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f384', u'\U0001f385',
        u'\U0001f9d9'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f9d9',
        u'\U0001f9d9'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f9dd'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f',
        u'\U0001f9dd', u'\U0001f9dd'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f9db'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f9db',
        u'\U0001f9db'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f9df'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f',
        u'\U0001f9df', u'\U0001f9df'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f9de'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f9de',
        u'\U0001f9de'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f9dc'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f',
        u'\U0001f9dc', u'\U0001f9dc'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f9da'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f9da',
        u'\U0001f9da'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f47c',
        u'\U0001f930', u'\U0001f931', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f37c',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f37c',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f37c',
        u'\U0001f647'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f647',
        u'\U0001f647'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f481'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f481',
        u'\U0001f481'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f645'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f645',
        u'\U0001f645'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f646'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f',
        u'\U0001f646', u'\U0001f646'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f64b'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f64b',
        u'\U0001f64b'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f9cf'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f',
        u'\U0001f9cf', u'\U0001f9cf'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f926'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f926',
        u'\U0001f926'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f937'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f937',
        u'\U0001f937'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f64e'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f',
        u'\U0001f64e', u'\U0001f64e'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f64d'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f64d',
        u'\U0001f64d'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f487'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f487',
        u'\U0001f487'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f486'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f486',
        u'\U0001f486'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f9d6'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f',
        u'\U0001f9d6', u'\U0001f9d6'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f485', u'\U0001f933', u'\U0001f483', u'\U0001f57a',
        u'\U0001f46f'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f46f',
        u'\U0001f46f'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f574',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f9bd', u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f9bd',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f9bd', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f9bc',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f9bc', u'\U0001f468'+ u'\U0000200d'+ u'\U0001f9bc',
        u'\U0001f6b6'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f6b6',
        u'\U0001f6b6'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f9af', u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f9af',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f9af',
        u'\U0001f9ce'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f',
        u'\U0001f9ce', u'\U0001f9ce'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f3c3'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f3c3',
        u'\U0001f3c3'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f',
        u'\U0001f9cd'+ u'\U0000200d'+ u'\U00002640'+ u'\U0000fe0f', u'\U0001f9cd',
        u'\U0001f9cd'+ u'\U0000200d'+ u'\U00002642'+ u'\U0000fe0f', u'\U0001f46d',
        u'\U0001f9d1'+ u'\U0000200d'+ u'\U0001f91d'+ u'\U0000200d'+ u'\U0001f9d1',
        u'\U0001f46c', u'\U0001f46b', u'\U0001f469'+ u'\U0000200d'+ u'\U00002764'+ u'\U0000fe0f'+ u'\U0000200d'+ u'\U0001f469',
        u'\U0001f491', u'\U0001f468'+ u'\U0000200d'+ u'\U00002764'+ u'\U0000fe0f'+ u'\U0000200d'+ u'\U0001f468'u'\U0001f469'+ u'\U0000200d'+ u'\U00002764'+ u'\U0000fe0f'+ u'\U0000200d'+ u'\U0001f468',
        u'\U0001f48f', u'\U0001f46a', u'\U0001f468'+ u'\U0000200d'+ u'\U0001f469'+ u'\U0000200d'+ u'\U0001f466',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f469'+ u'\U0000200d'+ u'\U0001f467',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f469'+ u'\U0000200d'+ u'\U0001f467'+ u'\U0000200d'+ u'\U0001f466',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f469'+ u'\U0000200d'+ u'\U0001f466'+ u'\U0000200d'+ u'\U0001f466',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f469'+ u'\U0000200d'+ u'\U0001f467'+ u'\U0000200d'+ u'\U0001f467',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f468'+ u'\U0000200d'+ u'\U0001f466',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f468'+ u'\U0000200d'+ u'\U0001f467',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f468'+ u'\U0000200d'+ u'\U0001f467'+ u'\U0000200d'+ u'\U0001f466',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f468'+ u'\U0000200d'+ u'\U0001f466'+ u'\U0000200d'+ u'\U0001f466',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f468'+ u'\U0000200d'+ u'\U0001f467'+ u'\U0000200d'+ u'\U0001f467',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f469'+ u'\U0000200d'+ u'\U0001f466',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f469'+ u'\U0000200d'+ u'\U0001f467',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f469'+ u'\U0000200d'+ u'\U0001f467'+ u'\U0000200d'+ u'\U0001f466',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f469'+ u'\U0000200d'+ u'\U0001f466'+ u'\U0000200d'+ u'\U0001f466',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f469'+ u'\U0000200d'+ u'\U0001f467'+ u'\U0000200d'+ u'\U0001f467',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f466', u'\U0001f468'+ u'\U0000200d'+ u'\U0001f466'+ u'\U0000200d'+ u'\U0001f466',
        u'\U0001f469'+ u'\U0000200d'+ u'\U00002764'+ u'\U0000fe0f'+ u'\U0000200d'+ u'\U0001f48b'+ u'\U0000200d'+ u'\U0001f469'+ u'\U0001f468'+ u'\U0000200d'+ u'\U00002764'+ u'\U0000fe0f'+ u'\U0000200d'+ u'\U0001f48b'+ u'\U0000200d'+ u'\U0001f468'+ u'\U0001f469'+ u'\U0000200d'+ u'\U00002764'+ u'\U0000fe0f'+ u'\U0000200d'+  u'\U0001f48b'+ u'\U0000200d'+ u'\U0001f468',
        u'\U0001f468'+ u'\U0000200d'+ u'\U0001f467', u'\U0001f468'+ u'\U0000200d'+ u'\U0001f467'+ u'\U0000200d'+ u'\U0001f466', u'\U0001f468'+ u'\U0000200d'+ u'\U0001f467'+ u'\U0000200d'+ u'\U0001f467', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f466', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f466'+ u'\U0000200d'+ u'\U0001f466', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f467',
        u'\U0001f469'+ u'\U0000200d'+ u'\U0001f467'+ u'\U0000200d'+ u'\U0001f466', u'\U0001f469'+ u'\U0000200d'+ u'\U0001f467'+ u'\U0000200d'+ u'\U0001f467', u'\U0001f5e3', u'\U0001f464', u'\U0001f465', u'\U0001fac2',
        ]

    return render(request, 'emoji/emoji.html',
    {
        # 'christmas': christmas,
        # 'faces': faces,
        # 'gestures': gestures,
        # 'people': people
        # 'nature': nature
        # 'food': food
        'activity': activity 
    })
