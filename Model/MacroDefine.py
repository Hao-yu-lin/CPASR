# Define the mode of Edit Center
NONE_MODE = 0
REF_MODE  = 1
ROI_MODE  = 2

# Define the mode of mouse state
MOUSE_STATE_NONE        = 0
MOUSE_STATE_DRAW_POINTS = 1

LST_NEED_MOUSE_TRACKING = [REF_MODE, ROI_MODE]

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
SHOW_HIST_TYPE_DATA2 = 2
SHOW_HIST_TYPE_BOTH  = 3

DF_CONTOURS_VALUE           = 'dfcontoursvalue'

# InputParam
INPUT_PARAM_INT_X_SPACING          = 'inputparamintxspacing'
INPUT_PARAM_INT_X_MIN              = 'inputparamintxmin'
INPUT_PARAM_INT_X_MAX              = 'inputparamintxmax'
INPUT_PARAM_LST_NAME               = 'inputparamlstname'
INPUT_PARAM_BOOL_SHOW_AVG          = 'inputparamboolshowavg'
INPUT_PARAM_BOOL_SHOW_MEDIAN       = 'inputparamboolshowmedian'
INPUT_PARAM_BOOL_SHOW_STD          = 'inputparamboolshowstd'
INPUT_PARAM_BOOL_SHOW_CUMLINE      = 'inputparamboolshowcumline'
INPUT_PARAM_LST_DATA_INFO          = 'inputparamlstdata'
INPUT_PARAM_INT_INFO_TYPE          = 'inputparamintdatainfotype'
INPUT_PARAM_INT_HIST_TYPE          = 'inputparaminthisttype'

# Data info
INT_INDEX                   = 'Index'
INT_AREA                    = 'Area'
INT_DIAMETER                = 'Diameter'
INT_MIN                     = 'min'
INT_MAX                     = 'max'
INT_AVERAGE                 = 'average'
INT_MEDIAN                  = 'median'
INT_STD                     = 'std'
INT_TOTAL                   = 'total'
STR_DATA_NAME               = 'strdataname'

DIAMETER_TYPE = 0
AREA_TYPE     = 1

PERCENTAGE_TYPE = 0
NUMBER_TYPE = 1

dicStrUintText = {
    DIAMETER_TYPE: 'um',
    AREA_TYPE: 'mm^2'
}
