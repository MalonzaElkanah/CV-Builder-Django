"use strict";

$("#link-add-id").click(function(){
	var input_num = parseInt($("input[name='form_num']").val());
	input_num = input_num + 1;
	$("input[name='form_num']").val(''+input_num+'');

    var content = '<div class="row form-item">' +
        '<div class="col-md-5 mb-3">' +
            '<label class="form-label">Link Name</label>' +
            '<input type="text" class="form-control" name="name-link_'+input_num+'">' +
        '</div>' +
        '<div class="col-md-5 mb-3">' +
            '<label class="form-label">Link Url</label>' +
            '<input type="text" class="form-control" name="link-link_'+input_num+'">' +
        '</div>' +
        '<div class="col-md-2">' +
            '<a class="btn btn-danger trash" href="javascript:void(0);">DELETE</a>' +
        '</div>' +
    '</div>';
	
    $(".form-row").append(content);
    return false;
});

$("#edu-add-id").click(function(){
	var input_num = parseInt($("#edu_count").text());
	input_num = input_num + 1;
	$("#edu_count").text(''+input_num+'');
	$("input[name='edu_form_num']").val(''+input_num+'');

	var listcontent = '<div class="row form-row edu-cont">' +
        '<div class="col-12 col-md-10">' +
            '<div class="row form-row">' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Institution</label>' +
                        '<input type="text" class="form-control" name="institution-edu_'+input_num+'">' +
                    '</div>' +
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Location</label>' +
                        '<input type="text" class="form-control" name="location-edu_'+input_num+'">' +
                    '</div>' + 
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Study Area</label>' +
                        '<input type="text" class="form-control" name="study_area-edu_'+input_num+'" placeholder="Eg. Bachelor of Science">' +
                    '</div>' + 
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Study Type</label>' +
                        '<input type="text" class="form-control" name="study_type-edu_'+input_num+'" placeholder="Eg. Computer Science">' +
                    '</div>' + 
                '</div>' +

                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Start Date</label>' +
                        '<input type="text" class="form-control datepicker" name="start_date-edu_'+input_num+'" placeholder="YYYY-MM-DD">' +
                    '</div>'  +
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>End Date</label>' +
                        '<input type="text" class="form-control datepicker" name="end_date-edu_'+input_num+'" placeholder="YYYY-MM-DD">' +
                    '</div>' +
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>GPA</label>' +
                        '<input type="text" class="form-control" name="gpa-edu_'+input_num+'">' +
                    '</div>' +
                '</div>' + 
            '</div>' +
        '</div>' +
        '<div class="col-12 col-md-2">' +
            '<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
            '<a href="#" class="btn btn-danger trash deleteData">' +
                '<i class="far fa-trash-alt"></i>' +
            '</a>' +
        '</div>' +
    '</div>';

    $(".edu-info").append(listcontent);
    return false;
});

$("#work-add-id").click(function(){
    var input_num = parseInt($("#work_count").text());
    input_num = input_num + 1;
    $("#work_count").text(''+input_num+'');
    $("input[name='work_form_num']").val(''+input_num+'');

    var listcontent = '<div class="row form-row work-cont">' +
        '<div class="col-12 col-md-10">' +
            '<div class="row form-row">' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Company</label>' +
                        '<input type="text" class="form-control" name="company-work_'+input_num+'">' +
                    '</div>' + 
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Location</label>' +
                        '<input type="text" class="form-control" name="location-work_'+input_num+'">' +
                    '</div>' + 
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Position</label>' +
                        '<input type="text" class="form-control" name="position-work_'+input_num+'">' +
                    '</div>' + 
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Website</label>' +
                        '<input type="text" class="form-control" name="website-work_'+input_num+'">' +
                    '</div>' + 
                '</div>' +

                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Start Date</label>' +
                        '<input type="text" class="form-control datepicker" name="start_date-work_'+input_num+'" placeholder="YYYY-MM-DD">' +
                    '</div>' + 
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>End Date</label>' +
                        '<input type="text" class="form-control datepicker" name="end_date-work_'+input_num+'" placeholder="YYYY-MM-DD">' +
                    '</div>' + 
                '</div>' +
            '</div>' +
        '</div>' +
        '<div class="col-12 col-md-2">' +
            '<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
            '<a href="#" class="btn btn-danger trash deleteData">' +
                '<i class="far fa-trash-alt"></i>' +
            '</a>' +
        '</div>' +
    '</div>'; 

    $(".work-info").append(listcontent);
    return false;
});


$("#skill-add-id").click(function(){
    var input_num = parseInt($("#skill_count").text());
    input_num = input_num + 1;
    $("#skill_count").text(''+input_num+'');
    $("input[name='skill_form_num']").val(''+input_num+'');

    var listcontent = '<div class="row form-row skill-cont">' +
        '<div class="col-12 col-md-10">' +
            '<div class="row form-row">' +
                '<div class="col-12">' +
                    '<div class="form-group">' +
                        '<label>Name</label>' +
                        '<input type="text" class="form-control" name="name-skill_'+input_num+'">' +
                    '</div>' + 
                '</div>' +
            '</div>' +
        '</div>' +
        '<div class="col-12 col-md-2">' +
            '<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
            '<a href="#" class="btn btn-danger trash deleteData">' +
                '<i class="far fa-trash-alt"></i>' +
            '</a>' +
        '</div>' +
    '</div>';

    $(".skill-info").append(listcontent);
    return false;
});

$("#project-add-id").click(function(){
    var input_num = parseInt($("#project_count").text());
    input_num = input_num + 1;
    $("#project_count").text(''+input_num+'');
    $("input[name='project_form_num']").val(''+input_num+'');

    var listcontent = '<div class="row form-row project-cont">' +
        '<div class="col-12 col-md-10">' +
            '<div class="row form-row">' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Name</label>' +
                        '<input type="text" class="form-control" name="name-project_'+input_num+'">' +
                    '</div>' + 
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Link</label>' +
                        '<input type="text" class="form-control" name="url-project_'+input_num+'">' +
                    '</div>' + 
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Description</label>' +
                        '<textarea class="form-control" name="description-project_'+input_num+'"></textarea>' +
                    '</div>' + 
                '</div>' +
            '</div>' +
        '</div>' +
        '<div class="col-12 col-md-2">' +
            '<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
            '<a href="#" class="btn btn-danger trash deleteData">' +
                '<i class="far fa-trash-alt"></i>' +
            '</a>' +
        '</div>' +
    '</div>';

    $(".project-info").append(listcontent);
    return false;
});


$("#award-add-id").click(function(){
    var input_num = parseInt($("#award_count").text());
    input_num = input_num + 1;
    $("#award_count").text(''+input_num+'');
    $("input[name='award_form_num']").val(''+input_num+'');

    var listcontent = '<div class="row form-row award-cont">' +
        '<div class="col-12 col-md-10">' +
            '<div class="row form-row">' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Title</label>' +
                        '<input type="text" class="form-control" name="title-award_'+input_num+'">' +
                    '</div>' + 
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Date</label>' +
                        '<input type="text" class="form-control datepicker" name="date-award_'+input_num+'" placeholder="YYYY-MM-DD">' +
                    '</div>' +
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Awarder</label>' +
                        '<input type="text" class="form-control" name="awarder-award_'+input_num+'">' +
                    '</div>' + 
                '</div>' +
                '<div class="col-12 col-md-6">' +
                    '<div class="form-group">' +
                        '<label>Summary</label>' +
                        '<textarea class="form-control" name="summary-award_'+input_num+'"></textarea>' +
                    '</div>' + 
                '</div>' +
            '</div>' +
        '</div>' +
        '<div class="col-12 col-md-2">' +
            '<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
            '<a href="#" class="btn btn-danger trash deleteData">' +
                '<i class="far fa-trash-alt"></i>' +
            '</a>' +
        '</div>' +
    '</div>';
    $(".award-info").append(listcontent);
    return false;
});
/*
$(".experience-info").on('click','.trash', function () {
    $(this).closest('.experience-cont').remove();
    return false;
});*/

function addSubskill(x){
    var count_name = "#sub-skill_count"+x+"";
    var input_name = "sub-skill_form_num"+x+"";
    var input_num = parseInt($(count_name).text());
    input_num = input_num + 1; 
    $(count_name).text(''+input_num+'');
    $("input[name='"+input_name+"']").val(''+input_num+'');
    var subskill = '<div class="col-sm-10 col-md-4">' +
        '<div class="row form-row">' +
            '<div class="col-12">' +
                '<div class="form-group">' +
                    '<label>Sub-Skill</label>' +
                    '<input type="text" class="form-control" name="name-sub-skill-'+x+'_'+input_num+'" value="">' +
                '</div>' +
            '</div>' +
        '</div>' +
    '</div>' +
    '<div class="col-sm-2 col-md-2">' +
        '<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
        '<a href="#" class="btn btn-danger trash deleteData">' +
            '<i class="far fa-trash-alt"></i>' +
        '</a>' +
    '</div>'; 
    var container = ".sub-skill-"+x+"";
    $(container).append(subskill);
}

function addWorkHighlight(x){
    var count_name = "#work-highlight_count"+x+"";
    var input_name = "work-highlight_form_num"+x+"";
    var input_num = parseInt($(count_name).text());
    input_num = input_num + 1; 
    $(count_name).text(''+input_num+'');
    $("input[name='"+input_name+"']").val(''+input_num+'');
    var subskill = '<div class="col-10">' +
        '<div class="row form-row">' +
            '<div class="col-12">' +
                '<div class="form-group">' +
                    '<label>Highlight</label>' +
                    '<input type="text" class="form-control" name="name-work-highlight-'+x+'_'+input_num+'">' +
                '</div>' +
            '</div>' +
        '</div>' +
    '</div>' +
    '<div class="col-sm-2 col-md-2">' +
        '<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
        '<a href="#" class="btn btn-danger trash deleteData">' +
            '<i class="far fa-trash-alt"></i>' +
        '</a>' +
    '</div>'; 


    var container = ".work-highlight-"+x+"";
    $(container).append(subskill);
}

function addTechnologyUsed(x){
    var count_name = "#technology_count"+x+"";
    var input_name = "technology_form_num"+x+"";
    var input_num = parseInt($(count_name).text());
    input_num = input_num + 1; 
    $(count_name).text(''+input_num+'');
    $("input[name='"+input_name+"']").val(''+input_num+'');
    var subskill = '<div class="col-10">' +
        '<div class="row form-row">' +
            '<div class="col-12">' +
                '<div class="form-group">' +
                    '<label>Technology</label>' +
                    '<input type="text" class="form-control" name="name-technology-'+x+'_'+input_num+'">' +
                '</div>' +
            '</div>' +
        '</div>' +
    '</div>' +
    '<div class="col-sm-2 col-md-2">' +
        '<label class="d-md-block d-sm-none d-none">&nbsp;</label>' +
        '<a href="#" class="btn btn-danger trash deleteData">' +
            '<i class="far fa-trash-alt"></i>' +
        '</a>' +
    '</div>'; 


    var container = ".technology-"+x+"";
    $(container).append(subskill);
}
