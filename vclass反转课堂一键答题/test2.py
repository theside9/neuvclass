import re
html='''
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <link rel="icon" type="image/png" href="../../../res/i/ico.png" sizes="16x16">
    <title>翻转课堂</title>
    <link href="../../../resources/bootstrap/css/bootstrap-huan.css" rel="stylesheet">
    <link href="../../../resources/font-awesome/css/font-awesome.min.css" rel="stylesheet">
    <link href="../../../resources/css/style.css" rel="stylesheet">

    <link href="../../../resources/css/exam.css" rel="stylesheet">
    <link href="../../../resources/chart/morris.css" rel="stylesheet">
</head>
<body>
<div>
    <div class="container" style="min-height:500px;">

        <div class="row">
            <div class="col-xs-3">
                <ul class="nav default-sidenav">
                    <li>
                        <a href="/exam/finishExam.html"> <i class="fa fa-bar-chart-o"></i> 分析报告 </a>

                    </li>
                    <li class="active">
                        <a href="#"> <i class="fa fa-file-text"></i> 详细解答 </a>
                    </li>
                    <li>
                    <a href="javascript:void(0)" onclick="backClass();"> <i class="fa fa-home"></i> 返回课程 </a>
                    </li>
                </ul>

            </div>
            <div class="col-xs-9">
                <div class="page-header">
                    <h1 style="margin-left: -15px;"><i class="fa fa-file-text"></i> 详细解答 </h1>
                </div>
                <div class="page-content row">
                    <div class="def-bk" id="bk-exampaper">

                        <div class="expand-bk-content" id="bk-conent-exampaper">
                            <div id="exampaper-header">
                                <div id="exampaper-title">
                                    <i class="fa fa-send"></i>
                                    <span id="exampaper-title-name"> 模拟试卷 </span>

                                </div>
                            </div>
                            <ul id="exampaper-body" style="padding:0px;">

                                                                        <li class="question qt-singlechoice">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">singlechoice</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">1</span>
                                                <span>[单选题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">8</span><span>分)</span></span>
                                                <span class="question-id" style="display:none;">1</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">1. （）不是创业者必须具备的能力。</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item"><input type="radio" value="A" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">A、市场投机能力</span></li>
                                                    <li class="question-list-item"><input type="radio" value="B" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">B、组织管理能力</span></li>
                                                    <li class="question-list-item"><input type="radio" value="C" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">C、开拓创新能力</span></li>
                                                    <li class="question-list-item"><input type="radio" value="D" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">D、人际协调能力</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">A</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-singlechoice">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">singlechoice</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">1</span>
                                                <span>[单选题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">8</span><span>分)</span></span>
                                                <span class="question-id" style="display:none;">1</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">2、创业型人才的特征不包括（）。</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item"><input type="radio" value="A" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">A、具有强烈和丰富的创业精神</span></li>
                                                    <li class="question-list-item"><input type="radio" value="B" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">B、坚持持续不断学习</span></li>
                                                    <li class="question-list-item"><input type="radio" value="C" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">C、勇于承担</span></li>
                                                    <li class="question-list-item"><input type="radio" value="D" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">D、谨小慎微、不敢实践</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">D</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-singlechoice">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">singlechoice</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">1</span>
                                                <span>[单选题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">8</span><span>分)</span></span>
                                                <span class="question-id" style="display:none;">1</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">3、关于领导者的行为策略，下列说法错误的是（）。</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item"><input type="radio" value="A" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">A、团队需要权威主管</span></li>
                                                    <li class="question-list-item"><input type="radio" value="B" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">B、对待团队成员要完全依赖</span></li>
                                                    <li class="question-list-item"><input type="radio" value="C" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">C、善于沟通与倾听</span></li>
                                                    <li class="question-list-item"><input type="radio" value="D" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">D、公平感知利益分配</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">B</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-singlechoice">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">singlechoice</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">1</span>
                                                <span>[单选题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">8</span><span>分)</span></span>
                                                <span class="question-id" style="display:none;">1</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">4、谈判成功的黄金法则不包括（）</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item"><input type="radio" value="A" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">A、欲速则不达</span></li>
                                                    <li class="question-list-item"><input type="radio" value="B" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">B、利益和压力并用</span></li>
                                                    <li class="question-list-item"><input type="radio" value="C" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">C、谈判桌上人人平等</span></li>
                                                    <li class="question-list-item"><input type="radio" value="D" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">D、永远不让步</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">D</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-singlechoice">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">singlechoice</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">1</span>
                                                <span>[单选题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">8</span><span>分)</span></span>
                                                <span class="question-id" style="display:none;">1</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">5. 关于创业与创业者，下列说法有误的是（）。</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item"><input type="radio" value="A" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">A、创业者在创业前要做好准备，包括正确认识自己</span></li>
                                                    <li class="question-list-item"><input type="radio" value="B" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">B、并不是每个人都适合创业</span></li>
                                                    <li class="question-list-item"><input type="radio" value="C" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">C、创业与职业生涯规划息息相关</span></li>
                                                    <li class="question-list-item"><input type="radio" value="D" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">D、创业精神是与生俱来的，与后天培养无关</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">D</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-singlechoice">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">singlechoice</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">1</span>
                                                <span>[单选题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">8</span><span>分)</span></span>
                                                <span class="question-id" style="display:none;">1</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">6、大多数90后创业者的特点不包括（  ）</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item"><input type="radio" value="A" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">  A、生活条件较好</span></li>
                                                    <li class="question-list-item"><input type="radio" value="B" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">  B、向往自由</span></li>
                                                    <li class="question-list-item"><input type="radio" value="C" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">  C、受教育程度高</span></li>
                                                    <li class="question-list-item"><input type="radio" value="D" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">  D、经验丰富</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">D</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-singlechoice">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">singlechoice</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">1</span>
                                                <span>[单选题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">8</span><span>分)</span></span>
                                                <span class="question-id" style="display:none;">1</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">7、下列关于成功创业者特征的描述，错误的是（）。</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item"><input type="radio" value="A" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">A、自主性强，不愿意受约束</span></li>
                                                    <li class="question-list-item"><input type="radio" value="B" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">B、随性而为，做事往往没有特定目标</span></li>
                                                    <li class="question-list-item"><input type="radio" value="C" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">C、自控力强，能自我管理</span></li>
                                                    <li class="question-list-item"><input type="radio" value="D" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">D、善于发现机会，有商业直觉</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">B</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-singlechoice">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">singlechoice</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">1</span>
                                                <span>[单选题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">8</span><span>分)</span></span>
                                                <span class="question-id" style="display:none;">1</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">8、大学生创业素质不包括（）。</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item"><input type="radio" value="A" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">A、人文科学素质</span></li>
                                                    <li class="question-list-item"><input type="radio" value="B" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">B、身心健康素质</span></li>
                                                    <li class="question-list-item"><input type="radio" value="C" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">C、创新创业能力素质</span></li>
                                                    <li class="question-list-item"><input type="radio" value="D" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">D、随遇而安素质</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">D</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-singlechoice">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">singlechoice</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">1</span>
                                                <span>[单选题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">8</span><span>分)</span></span>
                                                <span class="question-id" style="display:none;">1</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">9、创业者进行创业更多的是在追求（）。</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item"><input type="radio" value="A" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">A、经济效益</span></li>
                                                    <li class="question-list-item"><input type="radio" value="B" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">B、社会效益</span></li>
                                                    <li class="question-list-item"><input type="radio" value="C" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">C、综合效益</span></li>
                                                    <li class="question-list-item"><input type="radio" value="D" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">D、自我实现</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">D</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-singlechoice">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">singlechoice</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">1</span>
                                                <span>[单选题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">8</span><span>分)</span></span>
                                                <span class="question-id" style="display:none;">1</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">10、创业型人才知识结构包括（）。</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item"><input type="radio" value="A" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">A、商业经济学领域知识</span></li>
                                                    <li class="question-list-item"><input type="radio" value="B" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">B、管理知识</span></li>
                                                    <li class="question-list-item"><input type="radio" value="C" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">C、政策与法律知识</span></li>
                                                    <li class="question-list-item"><input type="radio" value="D" name="question-radio1" class="question-input">
                                                        <span class="question-li-text">D、以上均对</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">D</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-trueorfalse">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">trueorfalse</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">4</span>
                                                <span>[判断题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">4</span><span>分)</span></span><span class="question-id" style="display:none;">4</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">11、在创业过程中，创业者的个人素质要远比项目和资金重要，只有一流的人才才能打造一流的企业。（）</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item">
                                                        <input type="radio" value="正确" name="question-radio2" class="question-input">
                                                        <span class="question-li-text">正确</span>
                                                    </li>
                                                    <li class="question-list-item">
                                                        <input type="radio" value="错误" name="question-radio2" class="question-input">
                                                        <span class="question-li-text">错误</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">正确</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-trueorfalse">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">trueorfalse</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">4</span>
                                                <span>[判断题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">4</span><span>分)</span></span><span class="question-id" style="display:none;">4</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">12、有长远的眼光和较强的抗压能力是创业者的共性。（）</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item">
                                                        <input type="radio" value="正确" name="question-radio2" class="question-input">
                                                        <span class="question-li-text">正确</span>
                                                    </li>
                                                    <li class="question-list-item">
                                                        <input type="radio" value="错误" name="question-radio2" class="question-input">
                                                        <span class="question-li-text">错误</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">正确</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-trueorfalse">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">trueorfalse</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">4</span>
                                                <span>[判断题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">4</span><span>分)</span></span><span class="question-id" style="display:none;">4</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">13、如果一个人在个人能力发展阶段做得非常扎实，那么后期他面临的问题就会相对较少。</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item">
                                                        <input type="radio" value="正确" name="question-radio2" class="question-input">
                                                        <span class="question-li-text">正确</span>
                                                    </li>
                                                    <li class="question-list-item">
                                                        <input type="radio" value="错误" name="question-radio2" class="question-input">
                                                        <span class="question-li-text">错误</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">正确</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-trueorfalse">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">trueorfalse</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">4</span>
                                                <span>[判断题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">4</span><span>分)</span></span><span class="question-id" style="display:none;">4</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">14、知识经济的到来和创业的转型对创业人员的素质要求越来越高，因此创业人群不断减少。</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item">
                                                        <input type="radio" value="正确" name="question-radio2" class="question-input">
                                                        <span class="question-li-text">正确</span>
                                                    </li>
                                                    <li class="question-list-item">
                                                        <input type="radio" value="错误" name="question-radio2" class="question-input">
                                                        <span class="question-li-text">错误</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">错误</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                        <li class="question qt-trueorfalse">
                                            <div class="question-title">
                                                <div class="question-title-icon"></div>
                                                <span class="question-no"></span>
                                                <span class="question-type" style="display: none;">trueorfalse</span>
                                                <span class="knowledge-point-id" style="display: none;">1</span>
                                                <span class="question-type-id" style="display: none;">4</span>
                                                <span>[判断题]</span>
                                                <span class="question-point-content"><span>(</span><span class="question-point">4</span><span>分)</span></span><span class="question-id" style="display:none;">4</span>
                                            </div>
                                            <form class="question-body">
                                                <p class="question-body-text">15、广义的创业者是指企业的创办人。（）</p>
                                                <ul class="question-opt-list">
                                                    <li class="question-list-item">
                                                        <input type="radio" value="正确" name="question-radio2" class="question-input">
                                                        <span class="question-li-text">正确</span>
                                                    </li>
                                                    <li class="question-list-item">
                                                        <input type="radio" value="错误" name="question-radio2" class="question-input">
                                                        <span class="question-li-text">错误</span></li>
                                                </ul>
                                            </form>
                                            <div class="answer-desc">
                                                <div class="answer-desc-summary">
                                                    <span>正确答案：</span>
                                                    <span class="answer_value">错误</span>
                                                    <br>
                                                    <span>  你的解答：</span>
                                                    <span></span>
                                                </div>
                                                <div class="answer-desc-detail">
                                                    <label class="label label-warning">
                                                        <i class="fa fa-flag"></i>
                                                        <span> 解析</span>
                                                    </label>
                                                    <div class="answer-desc-content">
                                                        <p></p>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>


                            </ul>
                            <div id="exampaper-footer" style="height: 187px;">


                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript" src="../../../resources/js/jquery/jquery-1.9.0.min.js"></script>
<script type="text/javascript" src="../../../resources/bootstrap/js/bootstrap.min.js"></script>
<script>

    function backClass() {
        var address = window.location.hostname;
        var port = window.location.port;
        var base = "http://"+address+":"+port+"/";
        window.location.href = base+"/course/list.html";
    }

    $(function() {
        if (window.history && window.history.pushState) {
            $(window).on('popstate', function () {
                window.history.pushState('forward', null, '#');
                window.history.forward(1);
            });
        }
        window.history.pushState('forward', null, '#');
        window.history.forward(1);
    })
</script>
</body>
</html>
'''
html=html.replace(" ","").replace("\n","")

print(html)


findqustype=re.compile("<span>\[(.*?)\]</span>")
findanswer=re.compile("<spanclass=\"answer_value\">(.*?)</span>")
findtitle=re.compile("<pclass=\"question-body-text\">(.*?)</p>")
findalll=re.compile("<span>\[(.*?)\]</span>.*?<pclass=\"question-body-text\">(.*?)</p>.*?<spanclass=\"answer_value\">(.*?)</span>")

print(findalll.findall(html))
