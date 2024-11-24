# Define the mode of Edit Center
NONE_MODE = 0
REF_MODE  = 1
ROI_MODE  = 2
DEL_MODE  = 3

# Define the mode of mouse state
MOUSE_STATE_NONE        = 0
MOUSE_STATE_DRAW_POINTS = 1

LST_NEED_MOUSE_TRACKING = [REF_MODE, ROI_MODE, DEL_MODE]

# View Mode
VIEW_ORIGIN_MODE    = 0
VIEW_MASK_MODE      = 1
VIEW_CONTOURS_MODE  = 2
VIEW_HISTOGRAM_MODE = 3

# Cnt Mode
CNT_BAR_MODE    = 0
CNT_HIST_MODE   = 1

# Histogram Def
SHOW_HIST_TYPE_NONE  = 0
SHOW_HIST_TYPE_DATA1 = 1
SHOW_HIST_TYPE_BOTH  = 2

DF_CONTOURS_VALUE           = 'dfcontoursvalue'

# InputParam
INPUT_PARAM_INT_X_SPACING          = 'inputparamintxspacing'
INPUT_PARAM_INT_X_MIN              = 'inputparamintxmin'
INPUT_PARAM_INT_X_MAX              = 'inputparamintxmax'
INPUT_PARAM_LST_NAME               = 'inputparamlstname'
INPUT_PARAM_BOOL_SHOW_AVG          = 'inputparamboolshowavg'
INPUT_PARAM_BOOL_SHOW_BOXPLOT      = 'inputparamboolshowboxplot'
INPUT_PARAM_BOOL_SHOW_CUMLINE      = 'inputparamboolshowcumline'
INPUT_PARAM_LST_DATA_INFO          = 'inputparamlstdata'
INPUT_PARAM_INT_INFO_TYPE          = 'inputparamintdatainfotype'
INPUT_PARAM_INT_HIST_TYPE          = 'inputparaminthisttype'
INPUT_PARAM_BOOL_SHOW_HIST_VALUE   = 'inputparamboolshowhistvalue'
INPUT_PARAM_LST_SHOW_CUMULATIVE    = 'inputparamlstshowcumulative'
INPUT_PARAM_BOOL_SHOW_BOX_VALUE    = 'inputparamboolshowboxvalue'
INPUT_PARAM_INT_DATA_INDEX         = 'inputparamintdataindex'
INPUT_PARAM_LST_SHOW_DATA          = 'inputparamlstshowdata'

# Data info
INT_INDEX                   = 'index'
INT_AREA                    = 'area'
INT_DIAMETER                = 'diameter'
INT_MIN                     = 'min'
INT_MAX                     = 'max'
INT_AVERAGE                 = 'average'
INT_MEDIAN                  = 'median'
INT_STD                     = 'std'
INT_TOTAL                   = 'total'
STR_DATA_NAME               = 'strdataname'
BOOL_SHOW_DATA              = 'boolshowdata'

DIAMETER_TYPE = 0
AREA_TYPE     = 1

PERCENTAGE_TYPE = 0
NUMBER_TYPE = 1

dicStrUintText = {
    DIAMETER_TYPE: 'um',
    AREA_TYPE: 'mm^2'
}
