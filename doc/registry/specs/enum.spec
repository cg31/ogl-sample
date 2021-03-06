# License Applicability. Except to the extent portions of this file are
# made subject to an alternative license as permitted in the SGI Free
# Software License B, Version 1.1 (the "License"), the contents of this
# file are subject only to the provisions of the License. You may not use
# this file except in compliance with the License. You may obtain a copy
# of the License at Silicon Graphics, Inc., attn: Legal Services, 1600
# Amphitheatre Parkway, Mountain View, CA 94043-1351, or at:
#
# http://oss.sgi.com/projects/FreeB
#
# Note that, as provided in the License, the Software is distributed on an
# "AS IS" basis, with ALL EXPRESS AND IMPLIED WARRANTIES AND CONDITIONS
# DISCLAIMED, INCLUDING, WITHOUT LIMITATION, ANY IMPLIED WARRANTIES AND
# CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A
# PARTICULAR PURPOSE, AND NON-INFRINGEMENT.
#
# Original Code. The Original Code is: OpenGL Sample Implementation,
# Version 1.2.1, released January 26, 2000, developed by Silicon Graphics,
# Inc. The Original Code is Copyright (c) 1991-2000 Silicon Graphics, Inc.
# Copyright in any portions created by third parties is as indicated
# elsewhere herein. All Rights Reserved.
#
# Additional Notice Provisions: This software was created using the
# OpenGL(R) version 1.2.1 Sample Implementation published by SGI, but has
# not been independently verified as being compliant with the OpenGL(R)
# version 1.2.1 Specification.
#
# $Date: 2000/05/30 07:11:57 $ $Revision: 1.4 $
# $Header: /home/pub/cvs/projects/ogl-sample/main/doc/registry/specs/enum.spec,v 1.4 2000/05/30 07:11:57 ljp Exp $

# This is the OpenGL enumerant registry.
#
# It is an extremely important file. Do not mess with it unless
# you know what you're doing and have permission to do so.
#
###############################################################################
#
# Before modifying this file, read the following:
#
#   ONLY SGI's ARB representative (currently Jon Leech, ljp@sgi.com) may
#   allocate new enumerants outside the 'experimental' range described
#   below. Any modifications to this file not performed by SGI are
#   incompatible with the OpenGL API. The master copy of the registry,
#   showing up-to-date enumerant allocations, is maintained in the
#   OpenGL registry at
#
#	http://oss.sgi.com/projects/ogl-sample/registry
#
#   The following guidelines are thus only for reference purposes
#   (unless you're SGI's ARB representative :-)
#
#   Enumerant values for extensions CANNOT be chosen arbitrarily, since
#   the enumerant value space is shared by all GL licensees. It is
#   therefore imperative that the procedures described in this file be
#   followed carefully when allocating extension enum values.
#
# - Use tabs, not spaces.
#
# - When adding enum values for a new extension, use existing extensions
#   as a guide.
#
# - When a vendor has committed to releasing a new extension and needs to
#   allocate enum values for that extension, the vendor may request that SGI
#   allocate a previously unallocated block of 16 enum values, in the range
#   0x8000-0xFFFF, for the vendor's exclusive use.
#
#   New enumerants MUST be allocated by request to Jon Leech in the
#   OpenGL engineering group. For reference, the registry is being
#   maintained in the OpenGL group's Perforce tree as of this writing.
#
# - The vendor that introduces an extension will allocate enum values for
#   it as if it is a single-vendor extension, even if it is a multi-vendor
#   (EXT) extension.
#
# - The file enum.spec is principally a reference. The file enumext.spec
#   contains enumerants for all OpenGL 1.2 and OpenGL extensions in a form
#   used to generate <GL/glext.h>.
#
# - If a vendor hasn't yet released an extension, just add a comment to
#   enum.spec that contains the name of the extension and the range of enum
#   values used by the extension. When the vendor releases the extension,
#   put the actual enum assignments in enum.spec and enumext.spec.
#
# - Allocate all of the enum values for an extension in a single contiguous
#   block.
#
# - If an extension is experimental, allocate temporary enum values in the
#   range 0x6000-0x8000 during development work.  When the vendor commits to
#   releasing the extension, allocate permanent enum values (see below).
#   There are two reasons for this policy:
#
#   1.	It is desirable to keep extension enum values tightly packed and to
#	make all of the enum values for an extension be contiguous.  This is
#	possible only if permanent enum values for a new extension are not
#	allocated until the extension spec is stable and the number of new
#	enum values needed by the extension has therefore stopped changing.
#
#   2.	OpenGL ARB policy is that a vendor may allocate a new block of 16
#	extension enum values only if it has committed to releasing an
#	extension that will use values in that block.
#
# - To allocate a new block of permanent enum values for an extension, do the
#   following:
#
#   1.	Start at the top of enum.spec and choose the first SGI_future_use
#	range that is large enough to contain the new block.
#
#   2.	Allocate a block of enum values at the start of this range.  If
#	the enum definitions are going into enumfuture.spec, add a comment
#	to enum.spec that contains the name of the extension and
#	the range of values in the new block.	Use existing extensions
#	as a guide.
#
#   3.	Add the size of the block you just allocated to the start of the
#	chosen SGI_future_use range.  If you have allocated the entire
#	SGI_future_use range, eliminate the entry for this range in
#	enum.spec.
#
#   4.	If there are now no SGI_future_use ranges in enum.spec, follow
#	the instructions near the bottom of enum.spec to create a new one.
#	Note that there are historical enum allocations above 0xFFFF
#	but no new allocations will be performed there in the forseeable
#	future.
#
###############################################################################

Extensions define:
	VERSION_1_1					= 1
	VERSION_1_2					= 1
	ARB_imaging					= 1
	EXT_abgr					= 1
	EXT_blend_color					= 1
	EXT_blend_logic_op				= 1
	EXT_blend_minmax				= 1
	EXT_blend_subtract				= 1
	EXT_cmyka					= 1
	EXT_convolution					= 1
	EXT_copy_texture				= 1
	EXT_histogram					= 1
	EXT_packed_pixels				= 1
	EXT_point_parameters				= 1
	EXT_polygon_offset				= 1
	EXT_rescale_normal				= 1
	EXT_shared_texture_palette			= 1
	EXT_subtexture					= 1
	EXT_texture					= 1
	EXT_texture3D					= 1
	EXT_texture_object				= 1
	EXT_vertex_array				= 1
	SGIS_detail_texture				= 1
	SGIS_fog_function				= 1
	SGIS_generate_mipmap				= 1
	SGIS_multisample				= 1
	SGIS_pixel_texture				= 1
	SGIS_point_line_texgen				= 1
	SGIS_point_parameters				= 1
	SGIS_sharpen_texture				= 1
	SGIS_texture4D					= 1
	SGIS_texture_border_clamp			= 1
	SGIS_texture_edge_clamp				= 1
	SGIS_texture_filter4				= 1
	SGIS_texture_lod				= 1
	SGIS_texture_select				= 1
	SGIX_async					= 1
	SGIX_async_histogram				= 1
	SGIX_async_pixel				= 1
	SGIX_blend_alpha_minmax				= 1
	SGIX_calligraphic_fragment			= 1
	SGIX_clipmap					= 1
	SGIX_convolution_accuracy			= 1
	SGIX_depth_texture				= 1
	SGIX_flush_raster				= 1
	SGIX_fog_offset					= 1
	SGIX_fragment_lighting				= 1
	SGIX_framezoom					= 1
	SGIX_icc_texture				= 1
	SGIX_impact_pixel_texture			= 1
	SGIX_instruments				= 1
	SGIX_interlace					= 1
	SGIX_ir_instrument1				= 1
	SGIX_list_priority				= 1
	SGIX_pixel_texture				= 1
	SGIX_pixel_tiles				= 1
	SGIX_polynomial_ffd				= 1
	SGIX_reference_plane				= 1
	SGIX_resample					= 1
	SGIX_shadow					= 1
	SGIX_shadow_ambient				= 1
	SGIX_sprite					= 1
	SGIX_subsample					= 1
	SGIX_tag_sample_buffer				= 1
	SGIX_texture_add_env				= 1
	SGIX_texture_coordinate_clamp			= 1
	SGIX_texture_lod_bias				= 1
	SGIX_texture_multi_buffer			= 1
	SGIX_texture_scale_bias				= 1
	SGIX_vertex_preclip				= 1
	SGIX_ycrcb					= 1
	SGI_color_matrix				= 1
	SGI_color_table					= 1
	SGI_texture_color_table				= 1

###############################################################################

AttribMask enum:
	CURRENT_BIT					= 0x00000001
	POINT_BIT					= 0x00000002
	LINE_BIT					= 0x00000004
	POLYGON_BIT					= 0x00000008
	POLYGON_STIPPLE_BIT				= 0x00000010
	PIXEL_MODE_BIT					= 0x00000020
	LIGHTING_BIT					= 0x00000040
	FOG_BIT						= 0x00000080
	DEPTH_BUFFER_BIT				= 0x00000100
	ACCUM_BUFFER_BIT				= 0x00000200
	STENCIL_BUFFER_BIT				= 0x00000400
	VIEWPORT_BIT					= 0x00000800
	TRANSFORM_BIT					= 0x00001000
	ENABLE_BIT					= 0x00002000
	COLOR_BUFFER_BIT				= 0x00004000
	HINT_BIT					= 0x00008000
	EVAL_BIT					= 0x00010000
	LIST_BIT					= 0x00020000
	TEXTURE_BIT					= 0x00040000
	SCISSOR_BIT					= 0x00080000
	ALL_ATTRIB_BITS					= 0x000fffff
	MULTISAMPLE_BIT_EXT				= 0x20000000
#	use 3DFX_multisample MULTISAMPLE_BIT_3DFX
#	use ARB_multisample MULTISAMPLE_BIT_ARB

# 3DFX_multisample enum:
#	MULTISAMPLE_BIT_3DFX				= 0x20000000

# ARB_multisample enum:
#	MULTISAMPLE_BIT_ARB				= 0x20000000

###############################################################################

ClearBufferMask enum:
	use AttribMask COLOR_BUFFER_BIT
	use AttribMask ACCUM_BUFFER_BIT
	use AttribMask STENCIL_BUFFER_BIT
	use AttribMask DEPTH_BUFFER_BIT

###############################################################################

ClientAttribMask enum:
	CLIENT_PIXEL_STORE_BIT				= 0x00000001
	CLIENT_VERTEX_ARRAY_BIT				= 0x00000002
	CLIENT_ALL_ATTRIB_BITS				= 0xFFFFFFFF

###############################################################################

Boolean enum:
	FALSE						= 0
	TRUE						= 1

###############################################################################

BeginMode enum:
	POINTS						= 0x0000
	LINES						= 0x0001
	LINE_LOOP					= 0x0002
	LINE_STRIP					= 0x0003
	TRIANGLES					= 0x0004
	TRIANGLE_STRIP					= 0x0005
	TRIANGLE_FAN					= 0x0006
	QUADS						= 0x0007
	QUAD_STRIP					= 0x0008
	POLYGON						= 0x0009

###############################################################################

AccumOp enum:
	ACCUM						= 0x0100
	LOAD						= 0x0101
	RETURN						= 0x0102
	MULT						= 0x0103
	ADD						= 0x0104

###############################################################################

AlphaFunction enum:
	NEVER						= 0x0200
	LESS						= 0x0201
	EQUAL						= 0x0202
	LEQUAL						= 0x0203
	GREATER						= 0x0204
	NOTEQUAL					= 0x0205
	GEQUAL						= 0x0206
	ALWAYS						= 0x0207

###############################################################################

BlendingFactorDest enum:
	ZERO						= 0
	ONE						= 1
	SRC_COLOR					= 0x0300
	ONE_MINUS_SRC_COLOR				= 0x0301
	SRC_ALPHA					= 0x0302
	ONE_MINUS_SRC_ALPHA				= 0x0303
	DST_ALPHA					= 0x0304
	ONE_MINUS_DST_ALPHA				= 0x0305
	use EXT_blend_color CONSTANT_COLOR_EXT
	use EXT_blend_color ONE_MINUS_CONSTANT_COLOR_EXT
	use EXT_blend_color CONSTANT_ALPHA_EXT
	use EXT_blend_color ONE_MINUS_CONSTANT_ALPHA_EXT

###############################################################################

BlendingFactorSrc enum:
	use BlendingFactorDest ZERO
	use BlendingFactorDest ONE
	DST_COLOR					= 0x0306
	ONE_MINUS_DST_COLOR				= 0x0307
	SRC_ALPHA_SATURATE				= 0x0308
	use BlendingFactorDest SRC_ALPHA
	use BlendingFactorDest ONE_MINUS_SRC_ALPHA
	use BlendingFactorDest DST_ALPHA
	use BlendingFactorDest ONE_MINUS_DST_ALPHA
	use EXT_blend_color CONSTANT_COLOR_EXT
	use EXT_blend_color ONE_MINUS_CONSTANT_COLOR_EXT
	use EXT_blend_color CONSTANT_ALPHA_EXT
	use EXT_blend_color ONE_MINUS_CONSTANT_ALPHA_EXT

###############################################################################

BlendEquationModeEXT enum:
	use GetPName LOGIC_OP
	use EXT_blend_minmax FUNC_ADD_EXT
	use EXT_blend_minmax MIN_EXT
	use EXT_blend_minmax MAX_EXT
	use EXT_blend_subtract FUNC_SUBTRACT_EXT
	use EXT_blend_subtract FUNC_REVERSE_SUBTRACT_EXT
	use SGIX_blend_alpha_minmax ALPHA_MIN_SGIX
	use SGIX_blend_alpha_minmax ALPHA_MAX_SGIX

###############################################################################

ColorMaterialFace enum:
	use DrawBufferMode FRONT
	use DrawBufferMode BACK
	use DrawBufferMode FRONT_AND_BACK

###############################################################################

ColorMaterialParameter enum:
	use LightParameter AMBIENT
	use LightParameter DIFFUSE
	use LightParameter SPECULAR
	use MaterialParameter EMISSION
	use MaterialParameter AMBIENT_AND_DIFFUSE

###############################################################################

ColorPointerType enum:
	use DataType BYTE
	use DataType UNSIGNED_BYTE
	use DataType SHORT
	use DataType UNSIGNED_SHORT
	use DataType INT
	use DataType UNSIGNED_INT
	use DataType FLOAT
	use DataType DOUBLE

###############################################################################

ColorTableParameterPNameSGI enum:
	use SGI_color_table COLOR_TABLE_SCALE_SGI
	use SGI_color_table COLOR_TABLE_BIAS_SGI

###############################################################################

ColorTableTargetSGI enum:
	use SGI_color_table COLOR_TABLE_SGI
	use SGI_color_table POST_CONVOLUTION_COLOR_TABLE_SGI
	use SGI_color_table POST_COLOR_MATRIX_COLOR_TABLE_SGI
	use SGI_color_table PROXY_COLOR_TABLE_SGI
	use SGI_color_table PROXY_POST_CONVOLUTION_COLOR_TABLE_SGI
	use SGI_color_table PROXY_POST_COLOR_MATRIX_COLOR_TABLE_SGI
	use SGI_texture_color_table TEXTURE_COLOR_TABLE_SGI
	use SGI_texture_color_table PROXY_TEXTURE_COLOR_TABLE_SGI

###############################################################################

ConvolutionBorderModeEXT enum:
	use EXT_convolution REDUCE_EXT

###############################################################################

ConvolutionParameterEXT enum:
	use EXT_convolution CONVOLUTION_BORDER_MODE_EXT
	use EXT_convolution CONVOLUTION_FILTER_SCALE_EXT
	use EXT_convolution CONVOLUTION_FILTER_BIAS_EXT

###############################################################################

ConvolutionTargetEXT enum:
	use EXT_convolution CONVOLUTION_1D_EXT
	use EXT_convolution CONVOLUTION_2D_EXT

###############################################################################

CullFaceMode enum:
	use DrawBufferMode FRONT
	use DrawBufferMode BACK
	use DrawBufferMode FRONT_AND_BACK

###############################################################################

DepthFunction enum:
	use AlphaFunction NEVER
	use AlphaFunction LESS
	use AlphaFunction EQUAL
	use AlphaFunction LEQUAL
	use AlphaFunction GREATER
	use AlphaFunction NOTEQUAL
	use AlphaFunction GEQUAL
	use AlphaFunction ALWAYS

###############################################################################

DrawBufferMode enum:
	NONE						= 0
	FRONT_LEFT					= 0x0400
	FRONT_RIGHT					= 0x0401
	BACK_LEFT					= 0x0402
	BACK_RIGHT					= 0x0403
	FRONT						= 0x0404
	BACK						= 0x0405
	LEFT						= 0x0406
	RIGHT						= 0x0407
	FRONT_AND_BACK					= 0x0408
	AUX0						= 0x0409
	AUX1						= 0x040A
	AUX2						= 0x040B
	AUX3						= 0x040C

###############################################################################

EnableCap enum:
	use GetPName FOG
	use GetPName LIGHTING
	use GetPName TEXTURE_1D
	use GetPName TEXTURE_2D
	use GetPName LINE_STIPPLE
	use GetPName POLYGON_STIPPLE
	use GetPName CULL_FACE
	use GetPName ALPHA_TEST
	use GetPName BLEND
	use GetPName INDEX_LOGIC_OP
	use GetPName COLOR_LOGIC_OP
	use GetPName DITHER
	use GetPName STENCIL_TEST
	use GetPName DEPTH_TEST
	use GetPName CLIP_PLANE0
	use GetPName CLIP_PLANE1
	use GetPName CLIP_PLANE2
	use GetPName CLIP_PLANE3
	use GetPName CLIP_PLANE4
	use GetPName CLIP_PLANE5
	use GetPName LIGHT0
	use GetPName LIGHT1
	use GetPName LIGHT2
	use GetPName LIGHT3
	use GetPName LIGHT4
	use GetPName LIGHT5
	use GetPName LIGHT6
	use GetPName LIGHT7
	use GetPName TEXTURE_GEN_S
	use GetPName TEXTURE_GEN_T
	use GetPName TEXTURE_GEN_R
	use GetPName TEXTURE_GEN_Q
	use GetPName MAP1_VERTEX_3
	use GetPName MAP1_VERTEX_4
	use GetPName MAP1_COLOR_4
	use GetPName MAP1_INDEX
	use GetPName MAP1_NORMAL
	use GetPName MAP1_TEXTURE_COORD_1
	use GetPName MAP1_TEXTURE_COORD_2
	use GetPName MAP1_TEXTURE_COORD_3
	use GetPName MAP1_TEXTURE_COORD_4
	use GetPName MAP2_VERTEX_3
	use GetPName MAP2_VERTEX_4
	use GetPName MAP2_COLOR_4
	use GetPName MAP2_INDEX
	use GetPName MAP2_NORMAL
	use GetPName MAP2_TEXTURE_COORD_1
	use GetPName MAP2_TEXTURE_COORD_2
	use GetPName MAP2_TEXTURE_COORD_3
	use GetPName MAP2_TEXTURE_COORD_4
	use GetPName POINT_SMOOTH
	use GetPName LINE_SMOOTH
	use GetPName POLYGON_SMOOTH
	use GetPName SCISSOR_TEST
	use GetPName COLOR_MATERIAL
	use GetPName NORMALIZE
	use GetPName AUTO_NORMAL
	use GetPName POLYGON_OFFSET_POINT
	use GetPName POLYGON_OFFSET_LINE
	use GetPName POLYGON_OFFSET_FILL
	use GetPName VERTEX_ARRAY
	use GetPName NORMAL_ARRAY
	use GetPName COLOR_ARRAY
	use GetPName INDEX_ARRAY
	use GetPName TEXTURE_COORD_ARRAY
	use GetPName EDGE_FLAG_ARRAY
	use EXT_convolution CONVOLUTION_1D_EXT
	use EXT_convolution CONVOLUTION_2D_EXT
	use EXT_convolution SEPARABLE_2D_EXT
	use EXT_histogram HISTOGRAM_EXT
	use EXT_histogram MINMAX_EXT
	use EXT_rescale_normal RESCALE_NORMAL_EXT
	use EXT_shared_texture_palette SHARED_TEXTURE_PALETTE_EXT
	use EXT_texture3D TEXTURE_3D_EXT
	use SGIS_multisample MULTISAMPLE_SGIS
	use SGIS_multisample SAMPLE_ALPHA_TO_MASK_SGIS
	use SGIS_multisample SAMPLE_ALPHA_TO_ONE_SGIS
	use SGIS_multisample SAMPLE_MASK_SGIS
	use SGIS_texture4D TEXTURE_4D_SGIS
	use SGIX_async_histogram ASYNC_HISTOGRAM_SGIX
	use SGIX_async_pixel ASYNC_TEX_IMAGE_SGIX
	use SGIX_async_pixel ASYNC_DRAW_PIXELS_SGIX
	use SGIX_async_pixel ASYNC_READ_PIXELS_SGIX
	use SGIX_calligraphic_fragment CALLIGRAPHIC_FRAGMENT_SGIX
	use SGIX_fog_offset FOG_OFFSET_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHTING_SGIX
	use SGIX_fragment_lighting FRAGMENT_COLOR_MATERIAL_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT0_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT1_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT2_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT3_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT4_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT5_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT6_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT7_SGIX
	use SGIX_framezoom FRAMEZOOM_SGIX
	use SGIX_interlace INTERLACE_SGIX
	use SGIX_ir_instrument1 IR_INSTRUMENT1_SGIX
	use SGIX_pixel_texture PIXEL_TEX_GEN_SGIX
	use SGIS_pixel_texture PIXEL_TEXTURE_SGIS
	use SGIX_reference_plane REFERENCE_PLANE_SGIX
	use SGIX_sprite SPRITE_SGIX
	use SGI_color_table COLOR_TABLE_SGI
	use SGI_color_table POST_CONVOLUTION_COLOR_TABLE_SGI
	use SGI_color_table POST_COLOR_MATRIX_COLOR_TABLE_SGI
	use SGI_texture_color_table TEXTURE_COLOR_TABLE_SGI

###############################################################################

ErrorCode enum:
	NO_ERROR					= 0
	INVALID_ENUM					= 0x0500
	INVALID_VALUE					= 0x0501
	INVALID_OPERATION				= 0x0502
	STACK_OVERFLOW					= 0x0503
	STACK_UNDERFLOW					= 0x0504
	OUT_OF_MEMORY					= 0x0505
	use EXT_histogram TABLE_TOO_LARGE_EXT
	use EXT_texture TEXTURE_TOO_LARGE_EXT

###############################################################################

FeedbackType enum:
	2D						= 0x0600
	3D						= 0x0601
	3D_COLOR					= 0x0602
	3D_COLOR_TEXTURE				= 0x0603
	4D_COLOR_TEXTURE				= 0x0604

###############################################################################

FeedBackToken enum:
	PASS_THROUGH_TOKEN				= 0x0700
	POINT_TOKEN					= 0x0701
	LINE_TOKEN					= 0x0702
	POLYGON_TOKEN					= 0x0703
	BITMAP_TOKEN					= 0x0704
	DRAW_PIXEL_TOKEN				= 0x0705
	COPY_PIXEL_TOKEN				= 0x0706
	LINE_RESET_TOKEN				= 0x0707

###############################################################################

# Incomplete extension, not in enumext.spec
# FfdMaskSGIX enum:
#	TEXTURE_DEFORMATION_BIT_SGIX			= 0x00000001
#	GEOMETRY_DEFORMATION_BIT_SGIX			= 0x00000002

###############################################################################

# Incomplete extension, not in enumext.spec
# FfdTargetSGIX enum:
#	use SGIX_polynomial_ffd GEOMETRY_DEFORMATION_SGIX
#	use SGIX_polynomial_ffd TEXTURE_DEFORMATION_SGIX

###############################################################################

FogMode enum:
	use TextureMagFilter LINEAR
	EXP						= 0x0800
	EXP2						= 0x0801
	use SGIS_fog_function FOG_FUNC_SGIS

###############################################################################

FogParameter enum:
	use GetPName FOG_COLOR
	use GetPName FOG_DENSITY
	use GetPName FOG_END
	use GetPName FOG_INDEX
	use GetPName FOG_MODE
	use GetPName FOG_START
	use SGIX_fog_offset FOG_OFFSET_VALUE_SGIX

###############################################################################

FragmentLightModelParameterSGIX enum:
	use SGIX_fragment_lighting FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT_MODEL_TWO_SIDE_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT_MODEL_AMBIENT_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_SGIX

###############################################################################

FrontFaceDirection enum:
	CW						= 0x0900
	CCW						= 0x0901

###############################################################################

GetColorTableParameterPNameSGI enum:
	use SGI_color_table COLOR_TABLE_SCALE_SGI
	use SGI_color_table COLOR_TABLE_BIAS_SGI
	use SGI_color_table COLOR_TABLE_FORMAT_SGI
	use SGI_color_table COLOR_TABLE_WIDTH_SGI
	use SGI_color_table COLOR_TABLE_RED_SIZE_SGI
	use SGI_color_table COLOR_TABLE_GREEN_SIZE_SGI
	use SGI_color_table COLOR_TABLE_BLUE_SIZE_SGI
	use SGI_color_table COLOR_TABLE_ALPHA_SIZE_SGI
	use SGI_color_table COLOR_TABLE_LUMINANCE_SIZE_SGI
	use SGI_color_table COLOR_TABLE_INTENSITY_SIZE_SGI

###############################################################################

GetConvolutionParameter enum:
	use EXT_convolution CONVOLUTION_BORDER_MODE_EXT
	use EXT_convolution CONVOLUTION_FILTER_SCALE_EXT
	use EXT_convolution CONVOLUTION_FILTER_BIAS_EXT
	use EXT_convolution CONVOLUTION_FORMAT_EXT
	use EXT_convolution CONVOLUTION_WIDTH_EXT
	use EXT_convolution CONVOLUTION_HEIGHT_EXT
	use EXT_convolution MAX_CONVOLUTION_WIDTH_EXT
	use EXT_convolution MAX_CONVOLUTION_HEIGHT_EXT

###############################################################################

GetHistogramParameterPNameEXT enum:
	use EXT_histogram HISTOGRAM_WIDTH_EXT
	use EXT_histogram HISTOGRAM_FORMAT_EXT
	use EXT_histogram HISTOGRAM_RED_SIZE_EXT
	use EXT_histogram HISTOGRAM_GREEN_SIZE_EXT
	use EXT_histogram HISTOGRAM_BLUE_SIZE_EXT
	use EXT_histogram HISTOGRAM_ALPHA_SIZE_EXT
	use EXT_histogram HISTOGRAM_LUMINANCE_SIZE_EXT
	use EXT_histogram HISTOGRAM_SINK_EXT

###############################################################################

GetMapQuery enum:
	COEFF						= 0x0A00
	ORDER						= 0x0A01
	DOMAIN						= 0x0A02

###############################################################################

GetMinmaxParameterPNameEXT enum:
	use EXT_histogram MINMAX_FORMAT_EXT
	use EXT_histogram MINMAX_SINK_EXT

###############################################################################

GetPixelMap enum:
	PIXEL_MAP_I_TO_I				= 0x0C70
	PIXEL_MAP_S_TO_S				= 0x0C71
	PIXEL_MAP_I_TO_R				= 0x0C72
	PIXEL_MAP_I_TO_G				= 0x0C73
	PIXEL_MAP_I_TO_B				= 0x0C74
	PIXEL_MAP_I_TO_A				= 0x0C75
	PIXEL_MAP_R_TO_R				= 0x0C76
	PIXEL_MAP_G_TO_G				= 0x0C77
	PIXEL_MAP_B_TO_B				= 0x0C78
	PIXEL_MAP_A_TO_A				= 0x0C79

###############################################################################

GetPointervPName enum:
	VERTEX_ARRAY_POINTER				= 0x808E
	NORMAL_ARRAY_POINTER				= 0x808F
	COLOR_ARRAY_POINTER				= 0x8090
	INDEX_ARRAY_POINTER				= 0x8091
	TEXTURE_COORD_ARRAY_POINTER			= 0x8092
	EDGE_FLAG_ARRAY_POINTER				= 0x8093
	FEEDBACK_BUFFER_POINTER				= 0x0DF0
	SELECTION_BUFFER_POINTER			= 0x0DF3
	use SGIX_instruments INSTRUMENT_BUFFER_POINTER_SGIX

###############################################################################

# the columns after the comment symbol (#) indicate: number of params, type
# (F - float, D - double, I - integer) for the returned values
GetPName enum:
	CURRENT_COLOR					= 0x0B00 # 4 F
	CURRENT_INDEX					= 0x0B01 # 1 F
	CURRENT_NORMAL					= 0x0B02 # 3 F
	CURRENT_TEXTURE_COORDS				= 0x0B03 # 4 F
	CURRENT_RASTER_COLOR				= 0x0B04 # 4 F
	CURRENT_RASTER_INDEX				= 0x0B05 # 1 F
	CURRENT_RASTER_TEXTURE_COORDS			= 0x0B06 # 4 F
	CURRENT_RASTER_POSITION				= 0x0B07 # 4 F
	CURRENT_RASTER_POSITION_VALID			= 0x0B08 # 1 I
	CURRENT_RASTER_DISTANCE				= 0x0B09 # 1 F

	POINT_SMOOTH					= 0x0B10 # 1 I
	POINT_SIZE					= 0x0B11 # 1 F
	POINT_SIZE_RANGE				= 0x0B12 # 2 F
	POINT_SIZE_GRANULARITY				= 0x0B13 # 1 F

	LINE_SMOOTH					= 0x0B20 # 1 I
	LINE_WIDTH					= 0x0B21 # 1 F
	LINE_WIDTH_RANGE				= 0x0B22 # 2 F
	LINE_WIDTH_GRANULARITY				= 0x0B23 # 1 F
	LINE_STIPPLE					= 0x0B24 # 1 I
	LINE_STIPPLE_PATTERN				= 0x0B25 # 1 I
	LINE_STIPPLE_REPEAT				= 0x0B26 # 1 I
	use VERSION_1_2 SMOOTH_POINT_SIZE_RANGE
	use VERSION_1_2 SMOOTH_POINT_SIZE_GRANULARITY
	use VERSION_1_2 SMOOTH_LINE_WIDTH_RANGE
	use VERSION_1_2 SMOOTH_LINE_WIDTH_GRANULARITY
	use VERSION_1_2 ALIASED_POINT_SIZE_RANGE
	use VERSION_1_2 ALIASED_LINE_WIDTH_RANGE

	LIST_MODE					= 0x0B30 # 1 I
	MAX_LIST_NESTING				= 0x0B31 # 1 I
	LIST_BASE					= 0x0B32 # 1 I
	LIST_INDEX					= 0x0B33 # 1 I

	POLYGON_MODE					= 0x0B40 # 2 I
	POLYGON_SMOOTH					= 0x0B41 # 1 I
	POLYGON_STIPPLE					= 0x0B42 # 1 I
	EDGE_FLAG					= 0x0B43 # 1 I
	CULL_FACE					= 0x0B44 # 1 I
	CULL_FACE_MODE					= 0x0B45 # 1 I
	FRONT_FACE					= 0x0B46 # 1 I

	LIGHTING					= 0x0B50 # 1 I
	LIGHT_MODEL_LOCAL_VIEWER			= 0x0B51 # 1 I
	LIGHT_MODEL_TWO_SIDE				= 0x0B52 # 1 I
	LIGHT_MODEL_AMBIENT				= 0x0B53 # 4 F
	SHADE_MODEL					= 0x0B54 # 1 I
	COLOR_MATERIAL_FACE				= 0x0B55 # 1 I
	COLOR_MATERIAL_PARAMETER			= 0x0B56 # 1 I
	COLOR_MATERIAL					= 0x0B57 # 1 I

	FOG						= 0x0B60 # 1 I
	FOG_INDEX					= 0x0B61 # 1 I
	FOG_DENSITY					= 0x0B62 # 1 F
	FOG_START					= 0x0B63 # 1 F
	FOG_END						= 0x0B64 # 1 F
	FOG_MODE					= 0x0B65 # 1 I
	FOG_COLOR					= 0x0B66 # 4 F

	DEPTH_RANGE					= 0x0B70 # 2 F
	DEPTH_TEST					= 0x0B71 # 1 I
	DEPTH_WRITEMASK					= 0x0B72 # 1 I
	DEPTH_CLEAR_VALUE				= 0x0B73 # 1 F
	DEPTH_FUNC					= 0x0B74 # 1 I

	ACCUM_CLEAR_VALUE				= 0x0B80 # 4 F

	STENCIL_TEST					= 0x0B90 # 1 I
	STENCIL_CLEAR_VALUE				= 0x0B91 # 1 I
	STENCIL_FUNC					= 0x0B92 # 1 I
	STENCIL_VALUE_MASK				= 0x0B93 # 1 I
	STENCIL_FAIL					= 0x0B94 # 1 I
	STENCIL_PASS_DEPTH_FAIL				= 0x0B95 # 1 I
	STENCIL_PASS_DEPTH_PASS				= 0x0B96 # 1 I
	STENCIL_REF					= 0x0B97 # 1 I
	STENCIL_WRITEMASK				= 0x0B98 # 1 I

	MATRIX_MODE					= 0x0BA0 # 1 I
	NORMALIZE					= 0x0BA1 # 1 I
	VIEWPORT					= 0x0BA2 # 4 I
	MODELVIEW_STACK_DEPTH				= 0x0BA3 # 1 I
	PROJECTION_STACK_DEPTH				= 0x0BA4 # 1 I
	TEXTURE_STACK_DEPTH				= 0x0BA5 # 1 I
	MODELVIEW_MATRIX				= 0x0BA6 # 16 F
	PROJECTION_MATRIX				= 0x0BA7 # 16 F
	TEXTURE_MATRIX					= 0x0BA8 # 16 F

	ATTRIB_STACK_DEPTH				= 0x0BB0 # 1 I
	CLIENT_ATTRIB_STACK_DEPTH			= 0x0BB1 # 1 I

	ALPHA_TEST					= 0x0BC0 # 1 I
	ALPHA_TEST_FUNC					= 0x0BC1 # 1 I
	ALPHA_TEST_REF					= 0x0BC2 # 1 F

	DITHER						= 0x0BD0 # 1 I

	BLEND_DST					= 0x0BE0 # 1 I
	BLEND_SRC					= 0x0BE1 # 1 I
	BLEND						= 0x0BE2 # 1 I

	LOGIC_OP_MODE					= 0x0BF0 # 1 I
	INDEX_LOGIC_OP					= 0x0BF1 # 1 I
	LOGIC_OP					= 0x0BF1 # 1 I
	COLOR_LOGIC_OP					= 0x0BF2 # 1 I

	AUX_BUFFERS					= 0x0C00 # 1 I
	DRAW_BUFFER					= 0x0C01 # 1 I
	READ_BUFFER					= 0x0C02 # 1 I

	SCISSOR_BOX					= 0x0C10 # 4 I
	SCISSOR_TEST					= 0x0C11 # 1 I

	INDEX_CLEAR_VALUE				= 0x0C20 # 1 I
	INDEX_WRITEMASK					= 0x0C21 # 1 I
	COLOR_CLEAR_VALUE				= 0x0C22 # 4 F
	COLOR_WRITEMASK					= 0x0C23 # 4 I

	INDEX_MODE					= 0x0C30 # 1 I
	RGBA_MODE					= 0x0C31 # 1 I
	DOUBLEBUFFER					= 0x0C32 # 1 I
	STEREO						= 0x0C33 # 1 I

	RENDER_MODE					= 0x0C40 # 1 I

	PERSPECTIVE_CORRECTION_HINT			= 0x0C50 # 1 I
	POINT_SMOOTH_HINT				= 0x0C51 # 1 I
	LINE_SMOOTH_HINT				= 0x0C52 # 1 I
	POLYGON_SMOOTH_HINT				= 0x0C53 # 1 I
	FOG_HINT					= 0x0C54 # 1 I

	TEXTURE_GEN_S					= 0x0C60 # 1 I
	TEXTURE_GEN_T					= 0x0C61 # 1 I
	TEXTURE_GEN_R					= 0x0C62 # 1 I
	TEXTURE_GEN_Q					= 0x0C63 # 1 I

	PIXEL_MAP_I_TO_I_SIZE				= 0x0CB0 # 1 I
	PIXEL_MAP_S_TO_S_SIZE				= 0x0CB1 # 1 I
	PIXEL_MAP_I_TO_R_SIZE				= 0x0CB2 # 1 I
	PIXEL_MAP_I_TO_G_SIZE				= 0x0CB3 # 1 I
	PIXEL_MAP_I_TO_B_SIZE				= 0x0CB4 # 1 I
	PIXEL_MAP_I_TO_A_SIZE				= 0x0CB5 # 1 I
	PIXEL_MAP_R_TO_R_SIZE				= 0x0CB6 # 1 I
	PIXEL_MAP_G_TO_G_SIZE				= 0x0CB7 # 1 I
	PIXEL_MAP_B_TO_B_SIZE				= 0x0CB8 # 1 I
	PIXEL_MAP_A_TO_A_SIZE				= 0x0CB9 # 1 I

	UNPACK_SWAP_BYTES				= 0x0CF0 # 1 I
	UNPACK_LSB_FIRST				= 0x0CF1 # 1 I
	UNPACK_ROW_LENGTH				= 0x0CF2 # 1 I
	UNPACK_SKIP_ROWS				= 0x0CF3 # 1 I
	UNPACK_SKIP_PIXELS				= 0x0CF4 # 1 I
	UNPACK_ALIGNMENT				= 0x0CF5 # 1 I

	PACK_SWAP_BYTES					= 0x0D00 # 1 I
	PACK_LSB_FIRST					= 0x0D01 # 1 I
	PACK_ROW_LENGTH					= 0x0D02 # 1 I
	PACK_SKIP_ROWS					= 0x0D03 # 1 I
	PACK_SKIP_PIXELS				= 0x0D04 # 1 I
	PACK_ALIGNMENT					= 0x0D05 # 1 I

	MAP_COLOR					= 0x0D10 # 1 I
	MAP_STENCIL					= 0x0D11 # 1 I
	INDEX_SHIFT					= 0x0D12 # 1 I
	INDEX_OFFSET					= 0x0D13 # 1 I
	RED_SCALE					= 0x0D14 # 1 F
	RED_BIAS					= 0x0D15 # 1 F
	ZOOM_X						= 0x0D16 # 1 F
	ZOOM_Y						= 0x0D17 # 1 F
	GREEN_SCALE					= 0x0D18 # 1 F
	GREEN_BIAS					= 0x0D19 # 1 F
	BLUE_SCALE					= 0x0D1A # 1 F
	BLUE_BIAS					= 0x0D1B # 1 F
	ALPHA_SCALE					= 0x0D1C # 1 F
	ALPHA_BIAS					= 0x0D1D # 1 F
	DEPTH_SCALE					= 0x0D1E # 1 F
	DEPTH_BIAS					= 0x0D1F # 1 F

	MAX_EVAL_ORDER					= 0x0D30 # 1 I
	MAX_LIGHTS					= 0x0D31 # 1 I
	MAX_CLIP_PLANES					= 0x0D32 # 1 I
	MAX_TEXTURE_SIZE				= 0x0D33 # 1 I
	MAX_PIXEL_MAP_TABLE				= 0x0D34 # 1 I
	MAX_ATTRIB_STACK_DEPTH				= 0x0D35 # 1 I
	MAX_MODELVIEW_STACK_DEPTH			= 0x0D36 # 1 I
	MAX_NAME_STACK_DEPTH				= 0x0D37 # 1 I
	MAX_PROJECTION_STACK_DEPTH			= 0x0D38 # 1 I
	MAX_TEXTURE_STACK_DEPTH				= 0x0D39 # 1 I
	MAX_VIEWPORT_DIMS				= 0x0D3A # 2 F
	MAX_CLIENT_ATTRIB_STACK_DEPTH			= 0x0D3B # 1 I

	SUBPIXEL_BITS					= 0x0D50 # 1 I
	INDEX_BITS					= 0x0D51 # 1 I
	RED_BITS					= 0x0D52 # 1 I
	GREEN_BITS					= 0x0D53 # 1 I
	BLUE_BITS					= 0x0D54 # 1 I
	ALPHA_BITS					= 0x0D55 # 1 I
	DEPTH_BITS					= 0x0D56 # 1 I
	STENCIL_BITS					= 0x0D57 # 1 I
	ACCUM_RED_BITS					= 0x0D58 # 1 I
	ACCUM_GREEN_BITS				= 0x0D59 # 1 I
	ACCUM_BLUE_BITS					= 0x0D5A # 1 I
	ACCUM_ALPHA_BITS				= 0x0D5B # 1 I

	NAME_STACK_DEPTH				= 0x0D70 # 1 I

	AUTO_NORMAL					= 0x0D80 # 1 I

	MAP1_COLOR_4					= 0x0D90 # 1 I
	MAP1_INDEX					= 0x0D91 # 1 I
	MAP1_NORMAL					= 0x0D92 # 1 I
	MAP1_TEXTURE_COORD_1				= 0x0D93 # 1 I
	MAP1_TEXTURE_COORD_2				= 0x0D94 # 1 I
	MAP1_TEXTURE_COORD_3				= 0x0D95 # 1 I
	MAP1_TEXTURE_COORD_4				= 0x0D96 # 1 I
	MAP1_VERTEX_3					= 0x0D97 # 1 I
	MAP1_VERTEX_4					= 0x0D98 # 1 I

	MAP2_COLOR_4					= 0x0DB0 # 1 I
	MAP2_INDEX					= 0x0DB1 # 1 I
	MAP2_NORMAL					= 0x0DB2 # 1 I
	MAP2_TEXTURE_COORD_1				= 0x0DB3 # 1 I
	MAP2_TEXTURE_COORD_2				= 0x0DB4 # 1 I
	MAP2_TEXTURE_COORD_3				= 0x0DB5 # 1 I
	MAP2_TEXTURE_COORD_4				= 0x0DB6 # 1 I
	MAP2_VERTEX_3					= 0x0DB7 # 1 I
	MAP2_VERTEX_4					= 0x0DB8 # 1 I

	MAP1_GRID_DOMAIN				= 0x0DD0 # 2 F
	MAP1_GRID_SEGMENTS				= 0x0DD1 # 1 I
	MAP2_GRID_DOMAIN				= 0x0DD2 # 4 F
	MAP2_GRID_SEGMENTS				= 0x0DD3 # 2 I

	TEXTURE_1D					= 0x0DE0 # 1 I
	TEXTURE_2D					= 0x0DE1 # 1 I

	FEEDBACK_BUFFER_SIZE				= 0x0DF1 # 1 I
	FEEDBACK_BUFFER_TYPE				= 0x0DF2 # 1 I

	SELECTION_BUFFER_SIZE				= 0x0DF4 # 1 I

	POLYGON_OFFSET_UNITS				= 0x2A00 # 1 F
	POLYGON_OFFSET_POINT				= 0x2A01 # 1 I
	POLYGON_OFFSET_LINE				= 0x2A02 # 1 I
	POLYGON_OFFSET_FILL				= 0x8037 # 1 I
	POLYGON_OFFSET_FACTOR				= 0x8038 # 1 F

	TEXTURE_BINDING_1D				= 0x8068 # 1 I
	TEXTURE_BINDING_2D				= 0x8069 # 1 I
	TEXTURE_BINDING_3D				= 0x806A # 1 I

	VERTEX_ARRAY					= 0x8074 # 1 I
	NORMAL_ARRAY					= 0x8075 # 1 I
	COLOR_ARRAY					= 0x8076 # 1 I
	INDEX_ARRAY					= 0x8077 # 1 I
	TEXTURE_COORD_ARRAY				= 0x8078 # 1 I
	EDGE_FLAG_ARRAY					= 0x8079 # 1 I

	VERTEX_ARRAY_SIZE				= 0x807A # 1 I
	VERTEX_ARRAY_TYPE				= 0x807B # 1 I
	VERTEX_ARRAY_STRIDE				= 0x807C # 1 I

	NORMAL_ARRAY_TYPE				= 0x807E # 1 I
	NORMAL_ARRAY_STRIDE				= 0x807F # 1 I

	COLOR_ARRAY_SIZE				= 0x8081 # 1 I
	COLOR_ARRAY_TYPE				= 0x8082 # 1 I
	COLOR_ARRAY_STRIDE				= 0x8083 # 1 I

	INDEX_ARRAY_TYPE				= 0x8085 # 1 I
	INDEX_ARRAY_STRIDE				= 0x8086 # 1 I

	TEXTURE_COORD_ARRAY_SIZE			= 0x8088 # 1 I
	TEXTURE_COORD_ARRAY_TYPE			= 0x8089 # 1 I
	TEXTURE_COORD_ARRAY_STRIDE			= 0x808A # 1 I

	EDGE_FLAG_ARRAY_STRIDE				= 0x808C # 1 I

	use ClipPlaneName CLIP_PLANE0
	use ClipPlaneName CLIP_PLANE1
	use ClipPlaneName CLIP_PLANE2
	use ClipPlaneName CLIP_PLANE3
	use ClipPlaneName CLIP_PLANE4
	use ClipPlaneName CLIP_PLANE5

	use LightName LIGHT0
	use LightName LIGHT1
	use LightName LIGHT2
	use LightName LIGHT3
	use LightName LIGHT4
	use LightName LIGHT5
	use LightName LIGHT6
	use LightName LIGHT7

#	 use ARB_transpose_matrix TRANSPOSE_MODELVIEW_MATRIX_ARB
#	 use ARB_transpose_matrix TRANSPOSE_PROJECTION_MATRIX_ARB
#	 use ARB_transpose_matrix TRANSPOSE_TEXTURE_MATRIX_ARB
#	 use ARB_transpose_matrix TRANSPOSE_COLOR_MATRIX_ARB

	use VERSION_1_2 LIGHT_MODEL_COLOR_CONTROL

	use EXT_blend_color BLEND_COLOR_EXT

	use EXT_blend_minmax BLEND_EQUATION_EXT

	use EXT_cmyka PACK_CMYK_HINT_EXT
	use EXT_cmyka UNPACK_CMYK_HINT_EXT

	use EXT_convolution CONVOLUTION_1D_EXT
	use EXT_convolution CONVOLUTION_2D_EXT
	use EXT_convolution SEPARABLE_2D_EXT
	use EXT_convolution POST_CONVOLUTION_RED_SCALE_EXT
	use EXT_convolution POST_CONVOLUTION_GREEN_SCALE_EXT
	use EXT_convolution POST_CONVOLUTION_BLUE_SCALE_EXT
	use EXT_convolution POST_CONVOLUTION_ALPHA_SCALE_EXT
	use EXT_convolution POST_CONVOLUTION_RED_BIAS_EXT
	use EXT_convolution POST_CONVOLUTION_GREEN_BIAS_EXT
	use EXT_convolution POST_CONVOLUTION_BLUE_BIAS_EXT
	use EXT_convolution POST_CONVOLUTION_ALPHA_BIAS_EXT

	use EXT_histogram HISTOGRAM_EXT
	use EXT_histogram MINMAX_EXT

	use EXT_polygon_offset POLYGON_OFFSET_BIAS_EXT

	use EXT_rescale_normal RESCALE_NORMAL_EXT

	use EXT_shared_texture_palette SHARED_TEXTURE_PALETTE_EXT

	use EXT_texture_object TEXTURE_3D_BINDING_EXT

	use EXT_texture3D PACK_SKIP_IMAGES_EXT
	use EXT_texture3D PACK_IMAGE_HEIGHT_EXT
	use EXT_texture3D UNPACK_SKIP_IMAGES_EXT
	use EXT_texture3D UNPACK_IMAGE_HEIGHT_EXT
	use EXT_texture3D TEXTURE_3D_EXT
	use EXT_texture3D MAX_3D_TEXTURE_SIZE_EXT

	use EXT_vertex_array VERTEX_ARRAY_COUNT_EXT
	use EXT_vertex_array NORMAL_ARRAY_COUNT_EXT
	use EXT_vertex_array COLOR_ARRAY_COUNT_EXT
	use EXT_vertex_array INDEX_ARRAY_COUNT_EXT
	use EXT_vertex_array TEXTURE_COORD_ARRAY_COUNT_EXT
	use EXT_vertex_array EDGE_FLAG_ARRAY_COUNT_EXT

	use SGIS_detail_texture DETAIL_TEXTURE_2D_BINDING_SGIS

	use SGIS_fog_function FOG_FUNC_POINTS_SGIS
	use SGIS_fog_function MAX_FOG_FUNC_POINTS_SGIS

	use SGIS_generate_mipmap GENERATE_MIPMAP_HINT_SGIS

	use SGIS_multisample MULTISAMPLE_SGIS
	use SGIS_multisample SAMPLE_ALPHA_TO_MASK_SGIS
	use SGIS_multisample SAMPLE_ALPHA_TO_ONE_SGIS
	use SGIS_multisample SAMPLE_MASK_SGIS
	use SGIS_multisample SAMPLE_BUFFERS_SGIS
	use SGIS_multisample SAMPLES_SGIS
	use SGIS_multisample SAMPLE_MASK_VALUE_SGIS
	use SGIS_multisample SAMPLE_MASK_INVERT_SGIS
	use SGIS_multisample SAMPLE_PATTERN_SGIS

	use SGIS_pixel_texture PIXEL_TEXTURE_SGIS

	use SGIS_point_parameters POINT_SIZE_MIN_SGIS
	use SGIS_point_parameters POINT_SIZE_MAX_SGIS
	use SGIS_point_parameters POINT_FADE_THRESHOLD_SIZE_SGIS
	use SGIS_point_parameters DISTANCE_ATTENUATION_SGIS

	use SGIS_texture4D PACK_SKIP_VOLUMES_SGIS
	use SGIS_texture4D PACK_IMAGE_DEPTH_SGIS
	use SGIS_texture4D UNPACK_SKIP_VOLUMES_SGIS
	use SGIS_texture4D UNPACK_IMAGE_DEPTH_SGIS
	use SGIS_texture4D TEXTURE_4D_SGIS
	use SGIS_texture4D MAX_4D_TEXTURE_SIZE_SGIS
	use SGIS_texture4D TEXTURE_4D_BINDING_SGIS

	use SGIX_async ASYNC_MARKER_SGIX

	use SGIX_async_histogram ASYNC_HISTOGRAM_SGIX
	use SGIX_async_histogram MAX_ASYNC_HISTOGRAM_SGIX

	use SGIX_async_pixel ASYNC_TEX_IMAGE_SGIX
	use SGIX_async_pixel ASYNC_DRAW_PIXELS_SGIX
	use SGIX_async_pixel ASYNC_READ_PIXELS_SGIX
	use SGIX_async_pixel MAX_ASYNC_TEX_IMAGE_SGIX
	use SGIX_async_pixel MAX_ASYNC_DRAW_PIXELS_SGIX
	use SGIX_async_pixel MAX_ASYNC_READ_PIXELS_SGIX

	use SGIX_calligraphic_fragment CALLIGRAPHIC_FRAGMENT_SGIX

	use SGIX_clipmap MAX_CLIPMAP_VIRTUAL_DEPTH_SGIX
	use SGIX_clipmap MAX_CLIPMAP_DEPTH_SGIX

	use SGIX_convolution_accuracy CONVOLUTION_HINT_SGIX

	use SGIX_fog_offset FOG_OFFSET_SGIX
	use SGIX_fog_offset FOG_OFFSET_VALUE_SGIX

	use SGIX_fragment_lighting FRAGMENT_LIGHTING_SGIX
	use SGIX_fragment_lighting FRAGMENT_COLOR_MATERIAL_SGIX
	use SGIX_fragment_lighting FRAGMENT_COLOR_MATERIAL_FACE_SGIX
	use SGIX_fragment_lighting FRAGMENT_COLOR_MATERIAL_PARAMETER_SGIX
	use SGIX_fragment_lighting MAX_FRAGMENT_LIGHTS_SGIX
	use SGIX_fragment_lighting MAX_ACTIVE_LIGHTS_SGIX
	use SGIX_fragment_lighting LIGHT_ENV_MODE_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT_MODEL_TWO_SIDE_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT_MODEL_AMBIENT_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT0_SGIX

	use SGIX_framezoom FRAMEZOOM_SGIX
	use SGIX_framezoom FRAMEZOOM_FACTOR_SGIX
	use SGIX_framezoom MAX_FRAMEZOOM_FACTOR_SGIX

	use SGIX_instruments INSTRUMENT_MEASUREMENTS_SGIX

	use SGIX_interlace INTERLACE_SGIX

	use SGIX_ir_instrument1 IR_INSTRUMENT1_SGIX

	use SGIX_pixel_texture PIXEL_TEX_GEN_SGIX
	use SGIX_pixel_texture PIXEL_TEX_GEN_MODE_SGIX

	use SGIX_pixel_tiles PIXEL_TILE_BEST_ALIGNMENT_SGIX
	use SGIX_pixel_tiles PIXEL_TILE_CACHE_INCREMENT_SGIX
	use SGIX_pixel_tiles PIXEL_TILE_WIDTH_SGIX
	use SGIX_pixel_tiles PIXEL_TILE_HEIGHT_SGIX
	use SGIX_pixel_tiles PIXEL_TILE_GRID_WIDTH_SGIX
	use SGIX_pixel_tiles PIXEL_TILE_GRID_HEIGHT_SGIX
	use SGIX_pixel_tiles PIXEL_TILE_GRID_DEPTH_SGIX
	use SGIX_pixel_tiles PIXEL_TILE_CACHE_SIZE_SGIX

	use SGIX_polynomial_ffd DEFORMATIONS_MASK_SGIX

	use SGIX_reference_plane REFERENCE_PLANE_EQUATION_SGIX
	use SGIX_reference_plane REFERENCE_PLANE_SGIX

	use SGIX_sprite SPRITE_SGIX
	use SGIX_sprite SPRITE_MODE_SGIX
	use SGIX_sprite SPRITE_AXIS_SGIX
	use SGIX_sprite SPRITE_TRANSLATION_SGIX

	use SGIX_subsample PACK_SUBSAMPLE_RATE_SGIX
	use SGIX_subsample UNPACK_SUBSAMPLE_RATE_SGIX
	use SGIX_resample PACK_RESAMPLE_SGIX
	use SGIX_resample UNPACK_RESAMPLE_SGIX

	use SGIX_texture_scale_bias POST_TEXTURE_FILTER_BIAS_RANGE_SGIX
	use SGIX_texture_scale_bias POST_TEXTURE_FILTER_SCALE_RANGE_SGIX

	use SGIX_vertex_preclip VERTEX_PRECLIP_SGIX
	use SGIX_vertex_preclip VERTEX_PRECLIP_HINT_SGIX

	use SGI_color_matrix COLOR_MATRIX_SGI
	use SGI_color_matrix COLOR_MATRIX_STACK_DEPTH_SGI
	use SGI_color_matrix MAX_COLOR_MATRIX_STACK_DEPTH_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_RED_SCALE_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_GREEN_SCALE_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_BLUE_SCALE_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_ALPHA_SCALE_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_RED_BIAS_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_GREEN_BIAS_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_BLUE_BIAS_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_ALPHA_BIAS_SGI

	use SGI_color_table COLOR_TABLE_SGI
	use SGI_color_table POST_CONVOLUTION_COLOR_TABLE_SGI
	use SGI_color_table POST_COLOR_MATRIX_COLOR_TABLE_SGI

	use SGI_texture_color_table TEXTURE_COLOR_TABLE_SGI

###############################################################################

GetTextureParameter enum:
	use TextureParameterName TEXTURE_MAG_FILTER
	use TextureParameterName TEXTURE_MIN_FILTER
	use TextureParameterName TEXTURE_WRAP_S
	use TextureParameterName TEXTURE_WRAP_T
	TEXTURE_WIDTH					= 0x1000
	TEXTURE_HEIGHT					= 0x1001
	TEXTURE_INTERNAL_FORMAT				= 0x1003
	TEXTURE_COMPONENTS				= 0x1003
	TEXTURE_BORDER_COLOR				= 0x1004
	TEXTURE_BORDER					= 0x1005
	TEXTURE_RED_SIZE				= 0x805C
	TEXTURE_GREEN_SIZE				= 0x805D
	TEXTURE_BLUE_SIZE				= 0x805E
	TEXTURE_ALPHA_SIZE				= 0x805F
	TEXTURE_LUMINANCE_SIZE				= 0x8060
	TEXTURE_INTENSITY_SIZE				= 0x8061
	TEXTURE_PRIORITY				= 0x8066
	TEXTURE_RESIDENT				= 0x8067
	use EXT_texture3D TEXTURE_DEPTH_EXT
	use EXT_texture3D TEXTURE_WRAP_R_EXT
	use SGIS_detail_texture DETAIL_TEXTURE_LEVEL_SGIS
	use SGIS_detail_texture DETAIL_TEXTURE_MODE_SGIS
	use SGIS_detail_texture DETAIL_TEXTURE_FUNC_POINTS_SGIS
	use SGIS_generate_mipmap GENERATE_MIPMAP_SGIS
	use SGIS_sharpen_texture SHARPEN_TEXTURE_FUNC_POINTS_SGIS
	use SGIS_texture_filter4 TEXTURE_FILTER4_SIZE_SGIS
	use SGIS_texture_lod TEXTURE_MIN_LOD_SGIS
	use SGIS_texture_lod TEXTURE_MAX_LOD_SGIS
	use SGIS_texture_lod TEXTURE_BASE_LEVEL_SGIS
	use SGIS_texture_lod TEXTURE_MAX_LEVEL_SGIS
	use SGIS_texture_select DUAL_TEXTURE_SELECT_SGIS
	use SGIS_texture_select QUAD_TEXTURE_SELECT_SGIS
	use SGIS_texture4D TEXTURE_4DSIZE_SGIS
	use SGIS_texture4D TEXTURE_WRAP_Q_SGIS
	use SGIX_clipmap TEXTURE_CLIPMAP_CENTER_SGIX
	use SGIX_clipmap TEXTURE_CLIPMAP_FRAME_SGIX
	use SGIX_clipmap TEXTURE_CLIPMAP_OFFSET_SGIX
	use SGIX_clipmap TEXTURE_CLIPMAP_VIRTUAL_DEPTH_SGIX
	use SGIX_clipmap TEXTURE_CLIPMAP_LOD_OFFSET_SGIX
	use SGIX_clipmap TEXTURE_CLIPMAP_DEPTH_SGIX
	use SGIX_shadow TEXTURE_COMPARE_SGIX
	use SGIX_shadow TEXTURE_COMPARE_OPERATOR_SGIX
	use SGIX_shadow TEXTURE_LEQUAL_R_SGIX
	use SGIX_shadow TEXTURE_GEQUAL_R_SGIX
	use SGIX_shadow_ambient SHADOW_AMBIENT_SGIX
	use SGIX_texture_coordinate_clamp TEXTURE_MAX_CLAMP_S_SGIX
	use SGIX_texture_coordinate_clamp TEXTURE_MAX_CLAMP_T_SGIX
	use SGIX_texture_coordinate_clamp TEXTURE_MAX_CLAMP_R_SGIX
	use SGIX_texture_lod_bias TEXTURE_LOD_BIAS_S_SGIX
	use SGIX_texture_lod_bias TEXTURE_LOD_BIAS_T_SGIX
	use SGIX_texture_lod_bias TEXTURE_LOD_BIAS_R_SGIX
	use SGIX_texture_scale_bias POST_TEXTURE_FILTER_BIAS_SGIX
	use SGIX_texture_scale_bias POST_TEXTURE_FILTER_SCALE_SGIX

###############################################################################

HintMode enum:
	DONT_CARE					= 0x1100
	FASTEST						= 0x1101
	NICEST						= 0x1102

###############################################################################

HintTarget enum:
	use GetPName PERSPECTIVE_CORRECTION_HINT
	use GetPName POINT_SMOOTH_HINT
	use GetPName LINE_SMOOTH_HINT
	use GetPName POLYGON_SMOOTH_HINT
	use GetPName FOG_HINT
	use EXT_cmyka PACK_CMYK_HINT_EXT
	use EXT_cmyka UNPACK_CMYK_HINT_EXT
	use SGIS_generate_mipmap GENERATE_MIPMAP_HINT_SGIS
	use SGIX_convolution_accuracy CONVOLUTION_HINT_SGIX
	use SGIX_texture_multi_buffer TEXTURE_MULTI_BUFFER_HINT_SGIX
	use SGIX_vertex_preclip VERTEX_PRECLIP_HINT_SGIX

###############################################################################

HistogramTargetEXT enum:
	use EXT_histogram HISTOGRAM_EXT
	use EXT_histogram PROXY_HISTOGRAM_EXT

###############################################################################

IndexPointerType enum:
	use DataType SHORT
	use DataType INT
	use DataType FLOAT
	use DataType DOUBLE

###############################################################################

LightEnvModeSGIX enum:
	use StencilOp REPLACE
	use TextureEnvMode MODULATE
	use AccumOp ADD

###############################################################################

LightEnvParameterSGIX enum:
	use SGIX_fragment_lighting LIGHT_ENV_MODE_SGIX

###############################################################################

LightModelColorControl enum:
	use VERSION_1_2 SINGLE_COLOR
	use VERSION_1_2 SEPARATE_SPECULAR_COLOR

###############################################################################

LightModelParameter enum:
	use GetPName LIGHT_MODEL_AMBIENT
	use GetPName LIGHT_MODEL_LOCAL_VIEWER
	use GetPName LIGHT_MODEL_TWO_SIDE
	use VERSION_1_2 LIGHT_MODEL_COLOR_CONTROL

###############################################################################

LightParameter enum:
	AMBIENT						= 0x1200
	DIFFUSE						= 0x1201
	SPECULAR					= 0x1202
	POSITION					= 0x1203
	SPOT_DIRECTION					= 0x1204
	SPOT_EXPONENT					= 0x1205
	SPOT_CUTOFF					= 0x1206
	CONSTANT_ATTENUATION				= 0x1207
	LINEAR_ATTENUATION				= 0x1208
	QUADRATIC_ATTENUATION				= 0x1209

###############################################################################

ListMode enum:
	COMPILE						= 0x1300
	COMPILE_AND_EXECUTE				= 0x1301

###############################################################################

DataType enum:
	BYTE						= 0x1400
	UNSIGNED_BYTE					= 0x1401
	SHORT						= 0x1402
	UNSIGNED_SHORT					= 0x1403
	INT						= 0x1404
	UNSIGNED_INT					= 0x1405
	FLOAT						= 0x1406
	2_BYTES						= 0x1407
	3_BYTES						= 0x1408
	4_BYTES						= 0x1409
	DOUBLE						= 0x140A
	DOUBLE_EXT					= 0x140A

###############################################################################

ListNameType enum:
	use DataType BYTE
	use DataType UNSIGNED_BYTE
	use DataType SHORT
	use DataType UNSIGNED_SHORT
	use DataType INT
	use DataType UNSIGNED_INT
	use DataType FLOAT
	use DataType 2_BYTES
	use DataType 3_BYTES
	use DataType 4_BYTES

###############################################################################

ListParameterName enum:
	use SGIX_list_priority LIST_PRIORITY_SGIX

###############################################################################

LogicOp enum:
	CLEAR						= 0x1500
	AND						= 0x1501
	AND_REVERSE					= 0x1502
	COPY						= 0x1503
	AND_INVERTED					= 0x1504
	NOOP						= 0x1505
	XOR						= 0x1506
	OR						= 0x1507
	NOR						= 0x1508
	EQUIV						= 0x1509
	INVERT						= 0x150A
	OR_REVERSE					= 0x150B
	COPY_INVERTED					= 0x150C
	OR_INVERTED					= 0x150D
	NAND						= 0x150E
	SET						= 0x150F

###############################################################################

MapTarget enum:
	use GetPName MAP1_COLOR_4
	use GetPName MAP1_INDEX
	use GetPName MAP1_NORMAL
	use GetPName MAP1_TEXTURE_COORD_1
	use GetPName MAP1_TEXTURE_COORD_2
	use GetPName MAP1_TEXTURE_COORD_3
	use GetPName MAP1_TEXTURE_COORD_4
	use GetPName MAP1_VERTEX_3
	use GetPName MAP1_VERTEX_4
	use GetPName MAP2_COLOR_4
	use GetPName MAP2_INDEX
	use GetPName MAP2_NORMAL
	use GetPName MAP2_TEXTURE_COORD_1
	use GetPName MAP2_TEXTURE_COORD_2
	use GetPName MAP2_TEXTURE_COORD_3
	use GetPName MAP2_TEXTURE_COORD_4
	use GetPName MAP2_VERTEX_3
	use GetPName MAP2_VERTEX_4
	use SGIX_polynomial_ffd GEOMETRY_DEFORMATION_SGIX
	use SGIX_polynomial_ffd TEXTURE_DEFORMATION_SGIX

###############################################################################

MaterialFace enum:
	use DrawBufferMode FRONT
	use DrawBufferMode BACK
	use DrawBufferMode FRONT_AND_BACK


###############################################################################

MaterialParameter enum:
	EMISSION					= 0x1600
	SHININESS					= 0x1601
	AMBIENT_AND_DIFFUSE				= 0x1602
	COLOR_INDEXES					= 0x1603
	use LightProperty AMBIENT
	use LightProperty DIFFUSE
	use LightProperty SPECULAR

###############################################################################

MatrixMode enum:
	MODELVIEW					= 0x1700
	PROJECTION					= 0x1701
	TEXTURE						= 0x1702

###############################################################################

MeshMode1 enum:
	use PolygonMode POINT
	use PolygonMode LINE

###############################################################################

MeshMode2 enum:
	use PolygonMode POINT
	use PolygonMode LINE
	use PolygonMode FILL

###############################################################################

MinmaxTargetEXT enum:
	use EXT_histogram MINMAX_EXT

###############################################################################

NormalPointerType enum:
	use DataType BYTE
	use DataType SHORT
	use DataType INT
	use DataType FLOAT
	use DataType DOUBLE

###############################################################################

PixelCopyType enum:
	COLOR						= 0x1800
	DEPTH						= 0x1801
	STENCIL						= 0x1802

###############################################################################

PixelFormat enum:
	COLOR_INDEX					= 0x1900
	STENCIL_INDEX					= 0x1901
	DEPTH_COMPONENT					= 0x1902
	RED						= 0x1903
	GREEN						= 0x1904
	BLUE						= 0x1905
	ALPHA						= 0x1906
	RGB						= 0x1907
	RGBA						= 0x1908
	LUMINANCE					= 0x1909
	LUMINANCE_ALPHA					= 0x190A
	use EXT_abgr ABGR_EXT
	use EXT_cmyka CMYK_EXT
	use EXT_cmyka CMYKA_EXT
	use SGIX_icc_texture R5_G6_B5_ICC_SGIX
	use SGIX_icc_texture R5_G6_B5_A8_ICC_SGIX
	use SGIX_icc_texture ALPHA16_ICC_SGIX
	use SGIX_icc_texture LUMINANCE16_ICC_SGIX
	use SGIX_icc_texture LUMINANCE16_ALPHA8_ICC_SGIX
	use SGIX_ycrcb YCRCB_422_SGIX
	use SGIX_ycrcb YCRCB_444_SGIX

###############################################################################

PixelMap enum:
	use GetPixelMap PIXEL_MAP_I_TO_I
	use GetPixelMap PIXEL_MAP_S_TO_S
	use GetPixelMap PIXEL_MAP_I_TO_R
	use GetPixelMap PIXEL_MAP_I_TO_G
	use GetPixelMap PIXEL_MAP_I_TO_B
	use GetPixelMap PIXEL_MAP_I_TO_A
	use GetPixelMap PIXEL_MAP_R_TO_R
	use GetPixelMap PIXEL_MAP_G_TO_G
	use GetPixelMap PIXEL_MAP_B_TO_B
	use GetPixelMap PIXEL_MAP_A_TO_A

###############################################################################

PixelStoreParameter enum:
	use GetPName UNPACK_SWAP_BYTES
	use GetPName UNPACK_LSB_FIRST
	use GetPName UNPACK_ROW_LENGTH
	use GetPName UNPACK_SKIP_ROWS
	use GetPName UNPACK_SKIP_PIXELS
	use GetPName UNPACK_ALIGNMENT
	use GetPName PACK_SWAP_BYTES
	use GetPName PACK_LSB_FIRST
	use GetPName PACK_ROW_LENGTH
	use GetPName PACK_SKIP_ROWS
	use GetPName PACK_SKIP_PIXELS
	use GetPName PACK_ALIGNMENT
	use EXT_texture3D PACK_SKIP_IMAGES_EXT
	use EXT_texture3D PACK_IMAGE_HEIGHT_EXT
	use EXT_texture3D UNPACK_SKIP_IMAGES_EXT
	use EXT_texture3D UNPACK_IMAGE_HEIGHT_EXT
	use SGIS_texture4D PACK_SKIP_VOLUMES_SGIS
	use SGIS_texture4D PACK_IMAGE_DEPTH_SGIS
	use SGIS_texture4D UNPACK_SKIP_VOLUMES_SGIS
	use SGIS_texture4D UNPACK_IMAGE_DEPTH_SGIS
	use SGIX_pixel_tiles PIXEL_TILE_WIDTH_SGIX
	use SGIX_pixel_tiles PIXEL_TILE_HEIGHT_SGIX
	use SGIX_pixel_tiles PIXEL_TILE_GRID_WIDTH_SGIX
	use SGIX_pixel_tiles PIXEL_TILE_GRID_HEIGHT_SGIX
	use SGIX_pixel_tiles PIXEL_TILE_GRID_DEPTH_SGIX
	use SGIX_pixel_tiles PIXEL_TILE_CACHE_SIZE_SGIX
	use SGIX_subsample PACK_SUBSAMPLE_RATE_SGIX
	use SGIX_subsample UNPACK_SUBSAMPLE_RATE_SGIX
	use SGIX_resample PACK_RESAMPLE_SGIX
	use SGIX_resample UNPACK_RESAMPLE_SGIX

###############################################################################

PixelStoreResampleMode enum:
	use SGIX_resample RESAMPLE_REPLICATE_SGIX
	use SGIX_resample RESAMPLE_ZERO_FILL_SGIX
	use SGIX_resample RESAMPLE_DECIMATE_SGIX

###############################################################################

PixelStoreSubsampleRate enum:
	use SGIX_subsample PIXEL_SUBSAMPLE_4444_SGIX
	use SGIX_subsample PIXEL_SUBSAMPLE_2424_SGIX
	use SGIX_subsample PIXEL_SUBSAMPLE_4242_SGIX

###############################################################################

PixelTexGenMode enum:
	use DrawBufferMode NONE
	use PixelFormat RGB
	use PixelFormat RGBA
	use PixelFormat LUMINANCE
	use PixelFormat LUMINANCE_ALPHA
	use SGIX_impact_pixel_texture PIXEL_TEX_GEN_ALPHA_REPLACE_SGIX
	use SGIX_impact_pixel_texture PIXEL_TEX_GEN_ALPHA_NO_REPLACE_SGIX
	use SGIX_impact_pixel_texture PIXEL_TEX_GEN_ALPHA_MS_SGIX
	use SGIX_impact_pixel_texture PIXEL_TEX_GEN_ALPHA_LS_SGIX

###############################################################################

PixelTexGenParameterNameSGIS enum:
	use SGIS_pixel_texture PIXEL_FRAGMENT_RGB_SOURCE_SGIS
	use SGIS_pixel_texture PIXEL_FRAGMENT_ALPHA_SOURCE_SGIS

###############################################################################

PixelTransferParameter enum:
	use GetPName MAP_COLOR
	use GetPName MAP_STENCIL
	use GetPName INDEX_SHIFT
	use GetPName INDEX_OFFSET
	use GetPName RED_SCALE
	use GetPName RED_BIAS
	use GetPName GREEN_SCALE
	use GetPName GREEN_BIAS
	use GetPName BLUE_SCALE
	use GetPName BLUE_BIAS
	use GetPName ALPHA_SCALE
	use GetPName ALPHA_BIAS
	use GetPName DEPTH_SCALE
	use GetPName DEPTH_BIAS
	use EXT_convolution POST_CONVOLUTION_RED_SCALE_EXT
	use EXT_convolution POST_CONVOLUTION_GREEN_SCALE_EXT
	use EXT_convolution POST_CONVOLUTION_BLUE_SCALE_EXT
	use EXT_convolution POST_CONVOLUTION_ALPHA_SCALE_EXT
	use EXT_convolution POST_CONVOLUTION_RED_BIAS_EXT
	use EXT_convolution POST_CONVOLUTION_GREEN_BIAS_EXT
	use EXT_convolution POST_CONVOLUTION_BLUE_BIAS_EXT
	use EXT_convolution POST_CONVOLUTION_ALPHA_BIAS_EXT
	use SGI_color_matrix POST_COLOR_MATRIX_RED_SCALE_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_GREEN_SCALE_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_BLUE_SCALE_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_ALPHA_SCALE_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_RED_BIAS_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_GREEN_BIAS_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_BLUE_BIAS_SGI
	use SGI_color_matrix POST_COLOR_MATRIX_ALPHA_BIAS_SGI

###############################################################################

PixelType enum:
	BITMAP						= 0x1A00
	use DataType BYTE
	use DataType UNSIGNED_BYTE
	use DataType SHORT
	use DataType UNSIGNED_SHORT
	use DataType INT
	use DataType UNSIGNED_INT
	use DataType FLOAT
	use EXT_packed_pixels UNSIGNED_BYTE_3_3_2_EXT
	use EXT_packed_pixels UNSIGNED_SHORT_4_4_4_4_EXT
	use EXT_packed_pixels UNSIGNED_SHORT_5_5_5_1_EXT
	use EXT_packed_pixels UNSIGNED_INT_8_8_8_8_EXT
	use EXT_packed_pixels UNSIGNED_INT_10_10_10_2_EXT

###############################################################################

PointParameterNameSGIS enum:
	use SGIS_point_parameters POINT_SIZE_MIN_SGIS
	use SGIS_point_parameters POINT_SIZE_MAX_SGIS
	use SGIS_point_parameters POINT_FADE_THRESHOLD_SIZE_SGIS
	use SGIS_point_parameters DISTANCE_ATTENUATION_SGIS

###############################################################################

PolygonMode enum:
	POINT						= 0x1B00
	LINE						= 0x1B01
	FILL						= 0x1B02

###############################################################################

ReadBufferMode enum:
	use DrawBufferMode FRONT_LEFT
	use DrawBufferMode FRONT_RIGHT
	use DrawBufferMode BACK_LEFT
	use DrawBufferMode BACK_RIGHT
	use DrawBufferMode FRONT
	use DrawBufferMode BACK
	use DrawBufferMode LEFT
	use DrawBufferMode RIGHT
	use DrawBufferMode AUX0
	use DrawBufferMode AUX1
	use DrawBufferMode AUX2
	use DrawBufferMode AUX3

###############################################################################

RenderingMode enum:
	RENDER						= 0x1C00
	FEEDBACK					= 0x1C01
	SELECT						= 0x1C02

###############################################################################

SamplePatternSGIS enum:
	use SGIS_multisample 1PASS_SGIS
	use SGIS_multisample 2PASS_0_SGIS
	use SGIS_multisample 2PASS_1_SGIS
	use SGIS_multisample 4PASS_0_SGIS
	use SGIS_multisample 4PASS_1_SGIS
	use SGIS_multisample 4PASS_2_SGIS
	use SGIS_multisample 4PASS_3_SGIS

###############################################################################

SeparableTargetEXT enum:
	use EXT_convolution SEPARABLE_2D_EXT

###############################################################################

ShadingModel enum:
	FLAT						= 0x1D00
	SMOOTH						= 0x1D01

###############################################################################

StencilFunction enum:
	use AlphaFunction NEVER
	use AlphaFunction LESS
	use AlphaFunction EQUAL
	use AlphaFunction LEQUAL
	use AlphaFunction GREATER
	use AlphaFunction NOTEQUAL
	use AlphaFunction GEQUAL
	use AlphaFunction ALWAYS

###############################################################################

StencilOp enum:
	use BlendingFactorDest ZERO
	KEEP						= 0x1E00
	REPLACE						= 0x1E01
	INCR						= 0x1E02
	DECR						= 0x1E03
	use LogicOp INVERT

###############################################################################

StringName enum:
	VENDOR						= 0x1F00
	RENDERER					= 0x1F01
	VERSION						= 0x1F02
	EXTENSIONS					= 0x1F03

###############################################################################

TexCoordPointerType enum:
	use DataType SHORT
	use DataType INT
	use DataType FLOAT
	use DataType DOUBLE

###############################################################################

TextureCoordName enum:
	S						= 0x2000
	T						= 0x2001
	R						= 0x2002
	Q						= 0x2003

###############################################################################

TextureEnvMode enum:
	MODULATE					= 0x2100
	DECAL						= 0x2101
	use GetPName BLEND
	use EXT_texture REPLACE_EXT
	use AccumOp ADD
	use SGIX_texture_add_env TEXTURE_ENV_BIAS_SGIX

###############################################################################

TextureEnvParameter enum:
	TEXTURE_ENV_MODE				= 0x2200
	TEXTURE_ENV_COLOR				= 0x2201

###############################################################################

TextureEnvTarget enum:
	TEXTURE_ENV					= 0x2300

###############################################################################

TextureFilterFuncSGIS enum:
	use SGIS_texture_filter4 FILTER4_SGIS

###############################################################################

TextureGenMode enum:
	EYE_LINEAR					= 0x2400
	OBJECT_LINEAR					= 0x2401
	SPHERE_MAP					= 0x2402
	use SGIS_point_line_texgen EYE_DISTANCE_TO_POINT_SGIS
	use SGIS_point_line_texgen OBJECT_DISTANCE_TO_POINT_SGIS
	use SGIS_point_line_texgen EYE_DISTANCE_TO_LINE_SGIS
	use SGIS_point_line_texgen OBJECT_DISTANCE_TO_LINE_SGIS

###############################################################################

TextureGenParameter enum:
	TEXTURE_GEN_MODE				= 0x2500
	OBJECT_PLANE					= 0x2501
	EYE_PLANE					= 0x2502
	use SGIS_point_line_texgen EYE_POINT_SGIS
	use SGIS_point_line_texgen OBJECT_POINT_SGIS
	use SGIS_point_line_texgen EYE_LINE_SGIS
	use SGIS_point_line_texgen OBJECT_LINE_SGIS

###############################################################################

TextureMagFilter enum:
	NEAREST						= 0x2600
	LINEAR						= 0x2601
	use SGIS_detail_texture LINEAR_DETAIL_SGIS
	use SGIS_detail_texture LINEAR_DETAIL_ALPHA_SGIS
	use SGIS_detail_texture LINEAR_DETAIL_COLOR_SGIS
	use SGIS_sharpen_texture LINEAR_SHARPEN_SGIS
	use SGIS_sharpen_texture LINEAR_SHARPEN_ALPHA_SGIS
	use SGIS_sharpen_texture LINEAR_SHARPEN_COLOR_SGIS
	use SGIS_texture_filter4 FILTER4_SGIS
	use SGIX_impact_pixel_texture PIXEL_TEX_GEN_Q_CEILING_SGIX
	use SGIX_impact_pixel_texture PIXEL_TEX_GEN_Q_ROUND_SGIX
	use SGIX_impact_pixel_texture PIXEL_TEX_GEN_Q_FLOOR_SGIX

###############################################################################

TextureMinFilter enum:
	use TextureMagFilter NEAREST
	use TextureMagFilter LINEAR
	NEAREST_MIPMAP_NEAREST				= 0x2700
	LINEAR_MIPMAP_NEAREST				= 0x2701
	NEAREST_MIPMAP_LINEAR				= 0x2702
	LINEAR_MIPMAP_LINEAR				= 0x2703
	use SGIS_texture_filter4 FILTER4_SGIS
	use SGIX_clipmap LINEAR_CLIPMAP_LINEAR_SGIX
	use SGIX_clipmap NEAREST_CLIPMAP_NEAREST_SGIX
	use SGIX_clipmap NEAREST_CLIPMAP_LINEAR_SGIX
	use SGIX_clipmap LINEAR_CLIPMAP_NEAREST_SGIX
	use SGIX_impact_pixel_texture PIXEL_TEX_GEN_Q_CEILING_SGIX
	use SGIX_impact_pixel_texture PIXEL_TEX_GEN_Q_ROUND_SGIX
	use SGIX_impact_pixel_texture PIXEL_TEX_GEN_Q_FLOOR_SGIX

###############################################################################

TextureParameterName enum:
	TEXTURE_MAG_FILTER				= 0x2800
	TEXTURE_MIN_FILTER				= 0x2801
	TEXTURE_WRAP_S					= 0x2802
	TEXTURE_WRAP_T					= 0x2803
	use GetTextureParameter TEXTURE_BORDER_COLOR
	use GetTextureParameter TEXTURE_PRIORITY
	use EXT_texture3D TEXTURE_WRAP_R_EXT
	use SGIS_detail_texture DETAIL_TEXTURE_LEVEL_SGIS
	use SGIS_detail_texture DETAIL_TEXTURE_MODE_SGIS
	use SGIS_generate_mipmap GENERATE_MIPMAP_SGIS
	use SGIS_texture_select DUAL_TEXTURE_SELECT_SGIS
	use SGIS_texture_select QUAD_TEXTURE_SELECT_SGIS
	use SGIS_texture4D TEXTURE_WRAP_Q_SGIS
	use SGIX_clipmap TEXTURE_CLIPMAP_CENTER_SGIX
	use SGIX_clipmap TEXTURE_CLIPMAP_FRAME_SGIX
	use SGIX_clipmap TEXTURE_CLIPMAP_OFFSET_SGIX
	use SGIX_clipmap TEXTURE_CLIPMAP_VIRTUAL_DEPTH_SGIX
	use SGIX_clipmap TEXTURE_CLIPMAP_LOD_OFFSET_SGIX
	use SGIX_clipmap TEXTURE_CLIPMAP_DEPTH_SGIX
	use SGIX_shadow TEXTURE_COMPARE_SGIX
	use SGIX_shadow TEXTURE_COMPARE_OPERATOR_SGIX
	use SGIX_shadow_ambient SHADOW_AMBIENT_SGIX
	use SGIX_texture_coordinate_clamp TEXTURE_MAX_CLAMP_S_SGIX
	use SGIX_texture_coordinate_clamp TEXTURE_MAX_CLAMP_T_SGIX
	use SGIX_texture_coordinate_clamp TEXTURE_MAX_CLAMP_R_SGIX
	use SGIX_texture_lod_bias TEXTURE_LOD_BIAS_S_SGIX
	use SGIX_texture_lod_bias TEXTURE_LOD_BIAS_T_SGIX
	use SGIX_texture_lod_bias TEXTURE_LOD_BIAS_R_SGIX
	use SGIX_texture_scale_bias POST_TEXTURE_FILTER_BIAS_SGIX
	use SGIX_texture_scale_bias POST_TEXTURE_FILTER_SCALE_SGIX

###############################################################################

TextureTarget enum:
	use GetPName TEXTURE_1D
	use GetPName TEXTURE_2D
	PROXY_TEXTURE_1D				= 0x8063
	PROXY_TEXTURE_2D				= 0x8064
	use EXT_texture3D TEXTURE_3D_EXT
	use EXT_texture3D PROXY_TEXTURE_3D_EXT
	use SGIS_detail_texture DETAIL_TEXTURE_2D_SGIS
	use SGIS_texture4D TEXTURE_4D_SGIS
	use SGIS_texture4D PROXY_TEXTURE_4D_SGIS
	use SGIS_texture_lod TEXTURE_MIN_LOD_SGIS
	use SGIS_texture_lod TEXTURE_MAX_LOD_SGIS
	use SGIS_texture_lod TEXTURE_BASE_LEVEL_SGIS
	use SGIS_texture_lod TEXTURE_MAX_LEVEL_SGIS

###############################################################################

TextureWrapMode enum:
	CLAMP						= 0x2900
	REPEAT						= 0x2901
	use SGIS_texture_border_clamp CLAMP_TO_BORDER_SGIS
	use SGIS_texture_edge_clamp CLAMP_TO_EDGE_SGIS

###############################################################################

PixelInternalFormat enum:
	R3_G3_B2					= 0x2A10
	ALPHA4						= 0x803B
	ALPHA8						= 0x803C
	ALPHA12						= 0x803D
	ALPHA16						= 0x803E
	LUMINANCE4					= 0x803F
	LUMINANCE8					= 0x8040
	LUMINANCE12					= 0x8041
	LUMINANCE16					= 0x8042
	LUMINANCE4_ALPHA4				= 0x8043
	LUMINANCE6_ALPHA2				= 0x8044
	LUMINANCE8_ALPHA8				= 0x8045
	LUMINANCE12_ALPHA4				= 0x8046
	LUMINANCE12_ALPHA12				= 0x8047
	LUMINANCE16_ALPHA16				= 0x8048
	INTENSITY					= 0x8049
	INTENSITY4					= 0x804A
	INTENSITY8					= 0x804B
	INTENSITY12					= 0x804C
	INTENSITY16					= 0x804D
	RGB4						= 0x804F
	RGB5						= 0x8050
	RGB8						= 0x8051
	RGB10						= 0x8052
	RGB12						= 0x8053
	RGB16						= 0x8054
	RGBA2						= 0x8055
	RGBA4						= 0x8056
	RGB5_A1						= 0x8057
	RGBA8						= 0x8058
	RGB10_A2					= 0x8059
	RGBA12						= 0x805A
	RGBA16						= 0x805B
	use EXT_texture RGB2_EXT
	use SGIS_texture_select DUAL_ALPHA4_SGIS
	use SGIS_texture_select DUAL_ALPHA8_SGIS
	use SGIS_texture_select DUAL_ALPHA12_SGIS
	use SGIS_texture_select DUAL_ALPHA16_SGIS
	use SGIS_texture_select DUAL_LUMINANCE4_SGIS
	use SGIS_texture_select DUAL_LUMINANCE8_SGIS
	use SGIS_texture_select DUAL_LUMINANCE12_SGIS
	use SGIS_texture_select DUAL_LUMINANCE16_SGIS
	use SGIS_texture_select DUAL_INTENSITY4_SGIS
	use SGIS_texture_select DUAL_INTENSITY8_SGIS
	use SGIS_texture_select DUAL_INTENSITY12_SGIS
	use SGIS_texture_select DUAL_INTENSITY16_SGIS
	use SGIS_texture_select DUAL_LUMINANCE_ALPHA4_SGIS
	use SGIS_texture_select DUAL_LUMINANCE_ALPHA8_SGIS
	use SGIS_texture_select QUAD_ALPHA4_SGIS
	use SGIS_texture_select QUAD_ALPHA8_SGIS
	use SGIS_texture_select QUAD_LUMINANCE4_SGIS
	use SGIS_texture_select QUAD_LUMINANCE8_SGIS
	use SGIS_texture_select QUAD_INTENSITY4_SGIS
	use SGIS_texture_select QUAD_INTENSITY8_SGIS
	use SGIX_depth_texture DEPTH_COMPONENT16_SGIX
	use SGIX_depth_texture DEPTH_COMPONENT24_SGIX
	use SGIX_depth_texture DEPTH_COMPONENT32_SGIX
	use SGIX_icc_texture RGB_ICC_SGIX
	use SGIX_icc_texture RGBA_ICC_SGIX
	use SGIX_icc_texture ALPHA_ICC_SGIX
	use SGIX_icc_texture LUMINANCE_ICC_SGIX
	use SGIX_icc_texture INTENSITY_ICC_SGIX
	use SGIX_icc_texture LUMINANCE_ALPHA_ICC_SGIX
	use SGIX_icc_texture R5_G6_B5_ICC_SGIX
	use SGIX_icc_texture R5_G6_B5_A8_ICC_SGIX
	use SGIX_icc_texture ALPHA16_ICC_SGIX
	use SGIX_icc_texture LUMINANCE16_ICC_SGIX
	use SGIX_icc_texture INTENSITY16_ICC_SGIX
	use SGIX_icc_texture LUMINANCE16_ALPHA8_ICC_SGIX

###############################################################################

InterleavedArrayFormat enum:
	V2F						= 0x2A20
	V3F						= 0x2A21
	C4UB_V2F					= 0x2A22
	C4UB_V3F					= 0x2A23
	C3F_V3F						= 0x2A24
	N3F_V3F						= 0x2A25
	C4F_N3F_V3F					= 0x2A26
	T2F_V3F						= 0x2A27
	T4F_V4F						= 0x2A28
	T2F_C4UB_V3F					= 0x2A29
	T2F_C3F_V3F					= 0x2A2A
	T2F_N3F_V3F					= 0x2A2B
	T2F_C4F_N3F_V3F					= 0x2A2C
	T4F_C4F_N3F_V4F					= 0x2A2D

###############################################################################

VertexPointerType enum:
	use DataType SHORT
	use DataType INT
	use DataType FLOAT
	use DataType DOUBLE

###############################################################################

# 0x3000 through 0x3FFF are reserved for clip planes
ClipPlaneName enum:
	CLIP_PLANE0					= 0x3000 # 1 I
	CLIP_PLANE1					= 0x3001 # 1 I
	CLIP_PLANE2					= 0x3002 # 1 I
	CLIP_PLANE3					= 0x3003 # 1 I
	CLIP_PLANE4					= 0x3004 # 1 I
	CLIP_PLANE5					= 0x3005 # 1 I

###############################################################################

# 0x4000-0x4FFF are reserved for light numbers
LightName enum:
	LIGHT0						= 0x4000 # 1 I
	LIGHT1						= 0x4001 # 1 I
	LIGHT2						= 0x4002 # 1 I
	LIGHT3						= 0x4003 # 1 I
	LIGHT4						= 0x4004 # 1 I
	LIGHT5						= 0x4005 # 1 I
	LIGHT6						= 0x4006 # 1 I
	LIGHT7						= 0x4007 # 1 I
	use SGIX_fragment_lighting FRAGMENT_LIGHT0_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT1_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT2_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT3_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT4_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT5_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT6_SGIX
	use SGIX_fragment_lighting FRAGMENT_LIGHT7_SGIX

###############################################################################

EXT_abgr enum:
	ABGR_EXT					= 0x8000

###############################################################################

EXT_blend_color enum:
	CONSTANT_COLOR					= 0x8001
	CONSTANT_COLOR_EXT				= 0x8001
	ONE_MINUS_CONSTANT_COLOR			= 0x8002
	ONE_MINUS_CONSTANT_COLOR_EXT			= 0x8002
	CONSTANT_ALPHA					= 0x8003
	CONSTANT_ALPHA_EXT				= 0x8003
	ONE_MINUS_CONSTANT_ALPHA			= 0x8004
	ONE_MINUS_CONSTANT_ALPHA_EXT			= 0x8004
	BLEND_COLOR					= 0x8005 # 4 F
	BLEND_COLOR_EXT					= 0x8005 # 4 F

###############################################################################

EXT_blend_minmax enum:
	FUNC_ADD					= 0x8006
	FUNC_ADD_EXT					= 0x8006
	MIN						= 0x8007
	MIN_EXT						= 0x8007
	MAX						= 0x8008
	MAX_EXT						= 0x8008
	BLEND_EQUATION					= 0x8009 # 1 I
	BLEND_EQUATION_EXT				= 0x8009 # 1 I

###############################################################################

EXT_blend_subtract enum:
	FUNC_SUBTRACT					= 0x800A
	FUNC_SUBTRACT_EXT				= 0x800A
	FUNC_REVERSE_SUBTRACT				= 0x800B
	FUNC_REVERSE_SUBTRACT_EXT			= 0x800B

###############################################################################

EXT_cmyka enum:
	CMYK_EXT					= 0x800C
	CMYKA_EXT					= 0x800D
	PACK_CMYK_HINT_EXT				= 0x800E # 1 I
	UNPACK_CMYK_HINT_EXT				= 0x800F # 1 I

###############################################################################

EXT_convolution enum:
	CONVOLUTION_1D					= 0x8010 # 1 I
	CONVOLUTION_1D_EXT				= 0x8010 # 1 I
	CONVOLUTION_2D					= 0x8011 # 1 I
	CONVOLUTION_2D_EXT				= 0x8011 # 1 I
	SEPARABLE_2D					= 0x8012 # 1 I
	SEPARABLE_2D_EXT				= 0x8012 # 1 I
	CONVOLUTION_BORDER_MODE				= 0x8013
	CONVOLUTION_BORDER_MODE_EXT			= 0x8013
	CONVOLUTION_FILTER_SCALE			= 0x8014
	CONVOLUTION_FILTER_SCALE_EXT			= 0x8014
	CONVOLUTION_FILTER_BIAS				= 0x8015
	CONVOLUTION_FILTER_BIAS_EXT			= 0x8015
	REDUCE						= 0x8016
	REDUCE_EXT					= 0x8016
	CONVOLUTION_FORMAT				= 0x8017
	CONVOLUTION_FORMAT_EXT				= 0x8017
	CONVOLUTION_WIDTH				= 0x8018
	CONVOLUTION_WIDTH_EXT				= 0x8018
	CONVOLUTION_HEIGHT				= 0x8019
	CONVOLUTION_HEIGHT_EXT				= 0x8019
	MAX_CONVOLUTION_WIDTH				= 0x801A
	MAX_CONVOLUTION_WIDTH_EXT			= 0x801A
	MAX_CONVOLUTION_HEIGHT				= 0x801B
	MAX_CONVOLUTION_HEIGHT_EXT			= 0x801B
	POST_CONVOLUTION_RED_SCALE			= 0x801C # 1 F
	POST_CONVOLUTION_RED_SCALE_EXT			= 0x801C # 1 F
	POST_CONVOLUTION_GREEN_SCALE			= 0x801D # 1 F
	POST_CONVOLUTION_GREEN_SCALE_EXT		= 0x801D # 1 F
	POST_CONVOLUTION_BLUE_SCALE			= 0x801E # 1 F
	POST_CONVOLUTION_BLUE_SCALE_EXT			= 0x801E # 1 F
	POST_CONVOLUTION_ALPHA_SCALE			= 0x801F # 1 F
	POST_CONVOLUTION_ALPHA_SCALE_EXT		= 0x801F # 1 F
	POST_CONVOLUTION_RED_BIAS			= 0x8020 # 1 F
	POST_CONVOLUTION_RED_BIAS_EXT			= 0x8020 # 1 F
	POST_CONVOLUTION_GREEN_BIAS			= 0x8021 # 1 F
	POST_CONVOLUTION_GREEN_BIAS_EXT			= 0x8021 # 1 F
	POST_CONVOLUTION_BLUE_BIAS			= 0x8022 # 1 F
	POST_CONVOLUTION_BLUE_BIAS_EXT			= 0x8022 # 1 F
	POST_CONVOLUTION_ALPHA_BIAS			= 0x8023 # 1 F
	POST_CONVOLUTION_ALPHA_BIAS_EXT			= 0x8023 # 1 F

###############################################################################

EXT_histogram enum:
	HISTOGRAM					= 0x8024 # 1 I
	HISTOGRAM_EXT					= 0x8024 # 1 I
	PROXY_HISTOGRAM					= 0x8025
	PROXY_HISTOGRAM_EXT				= 0x8025
	HISTOGRAM_WIDTH					= 0x8026
	HISTOGRAM_WIDTH_EXT				= 0x8026
	HISTOGRAM_FORMAT				= 0x8027
	HISTOGRAM_FORMAT_EXT				= 0x8027
	HISTOGRAM_RED_SIZE				= 0x8028
	HISTOGRAM_RED_SIZE_EXT				= 0x8028
	HISTOGRAM_GREEN_SIZE				= 0x8029
	HISTOGRAM_GREEN_SIZE_EXT			= 0x8029
	HISTOGRAM_BLUE_SIZE				= 0x802A
	HISTOGRAM_BLUE_SIZE_EXT				= 0x802A
	HISTOGRAM_ALPHA_SIZE				= 0x802B
	HISTOGRAM_ALPHA_SIZE_EXT			= 0x802B
	HISTOGRAM_LUMINANCE_SIZE			= 0x802C
	HISTOGRAM_LUMINANCE_SIZE_EXT			= 0x802C
	HISTOGRAM_SINK					= 0x802D
	HISTOGRAM_SINK_EXT				= 0x802D
	MINMAX						= 0x802E # 1 I
	MINMAX_EXT					= 0x802E # 1 I
	MINMAX_FORMAT					= 0x802F
	MINMAX_FORMAT_EXT				= 0x802F
	MINMAX_SINK					= 0x8030
	MINMAX_SINK_EXT					= 0x8030
	TABLE_TOO_LARGE					= 0x8031
	TABLE_TOO_LARGE_EXT				= 0x8031

###############################################################################

EXT_packed_pixels enum:
	UNSIGNED_BYTE_3_3_2				= 0x8032
	UNSIGNED_BYTE_3_3_2_EXT				= 0x8032
	UNSIGNED_SHORT_4_4_4_4				= 0x8033
	UNSIGNED_SHORT_4_4_4_4_EXT			= 0x8033
	UNSIGNED_SHORT_5_5_5_1				= 0x8034
	UNSIGNED_SHORT_5_5_5_1_EXT			= 0x8034
	UNSIGNED_INT_8_8_8_8				= 0x8035
	UNSIGNED_INT_8_8_8_8_EXT			= 0x8035
	UNSIGNED_INT_10_10_10_2				= 0x8036
	UNSIGNED_INT_10_10_10_2_EXT			= 0x8036
	UNSIGNED_BYTE_2_3_3_REV				= 0x8362
	UNSIGNED_BYTE_2_3_3_REV_EXT			= 0x8362
	UNSIGNED_SHORT_5_6_5				= 0x8363
	UNSIGNED_SHORT_5_6_5_EXT			= 0x8363
	UNSIGNED_SHORT_5_6_5_REV			= 0x8364
	UNSIGNED_SHORT_5_6_5_REV_EXT			= 0x8364
	UNSIGNED_SHORT_4_4_4_4_REV			= 0x8365
	UNSIGNED_SHORT_4_4_4_4_REV_EXT			= 0x8365
	UNSIGNED_SHORT_1_5_5_5_REV			= 0x8366
	UNSIGNED_SHORT_1_5_5_5_REV_EXT			= 0x8366
	UNSIGNED_INT_8_8_8_8_REV			= 0x8367
	UNSIGNED_INT_8_8_8_8_REV_EXT			= 0x8367
	UNSIGNED_INT_2_10_10_10_REV			= 0x8368
	UNSIGNED_INT_2_10_10_10_REV_EXT			= 0x8368

###############################################################################

EXT_polygon_offset enum:
	POLYGON_OFFSET_EXT				= 0x8037
	POLYGON_OFFSET_FACTOR_EXT			= 0x8038
	POLYGON_OFFSET_BIAS_EXT				= 0x8039 # 1 F

###############################################################################

EXT_rescale_normal enum:
	RESCALE_NORMAL					= 0x803A # 1 I
	RESCALE_NORMAL_EXT				= 0x803A # 1 I

###############################################################################

EXT_texture enum:
	ALPHA4_EXT					= 0x803B
	ALPHA8_EXT					= 0x803C
	ALPHA12_EXT					= 0x803D
	ALPHA16_EXT					= 0x803E
	LUMINANCE4_EXT					= 0x803F
	LUMINANCE8_EXT					= 0x8040
	LUMINANCE12_EXT					= 0x8041
	LUMINANCE16_EXT					= 0x8042
	LUMINANCE4_ALPHA4_EXT				= 0x8043
	LUMINANCE6_ALPHA2_EXT				= 0x8044
	LUMINANCE8_ALPHA8_EXT				= 0x8045
	LUMINANCE12_ALPHA4_EXT				= 0x8046
	LUMINANCE12_ALPHA12_EXT				= 0x8047
	LUMINANCE16_ALPHA16_EXT				= 0x8048
	INTENSITY_EXT					= 0x8049
	INTENSITY4_EXT					= 0x804A
	INTENSITY8_EXT					= 0x804B
	INTENSITY12_EXT					= 0x804C
	INTENSITY16_EXT					= 0x804D
	RGB2_EXT					= 0x804E
	RGB4_EXT					= 0x804F
	RGB5_EXT					= 0x8050
	RGB8_EXT					= 0x8051
	RGB10_EXT					= 0x8052
	RGB12_EXT					= 0x8053
	RGB16_EXT					= 0x8054
	RGBA2_EXT					= 0x8055
	RGBA4_EXT					= 0x8056
	RGB5_A1_EXT					= 0x8057
	RGBA8_EXT					= 0x8058
	RGB10_A2_EXT					= 0x8059
	RGBA12_EXT					= 0x805A
	RGBA16_EXT					= 0x805B
	TEXTURE_RED_SIZE_EXT				= 0x805C
	TEXTURE_GREEN_SIZE_EXT				= 0x805D
	TEXTURE_BLUE_SIZE_EXT				= 0x805E
	TEXTURE_ALPHA_SIZE_EXT				= 0x805F
	TEXTURE_LUMINANCE_SIZE_EXT			= 0x8060
	TEXTURE_INTENSITY_SIZE_EXT			= 0x8061
	REPLACE_EXT					= 0x8062
	PROXY_TEXTURE_1D_EXT				= 0x8063
	PROXY_TEXTURE_2D_EXT				= 0x8064
	TEXTURE_TOO_LARGE_EXT				= 0x8065

###############################################################################

EXT_texture_object enum:
	TEXTURE_PRIORITY_EXT				= 0x8066
	TEXTURE_RESIDENT_EXT				= 0x8067
	TEXTURE_1D_BINDING_EXT				= 0x8068
	TEXTURE_2D_BINDING_EXT				= 0x8069
	TEXTURE_3D_BINDING_EXT				= 0x806A # 1 I

###############################################################################

EXT_texture3D enum:
	PACK_SKIP_IMAGES				= 0x806B # 1 I
	PACK_SKIP_IMAGES_EXT				= 0x806B # 1 I
	PACK_IMAGE_HEIGHT				= 0x806C # 1 F
	PACK_IMAGE_HEIGHT_EXT				= 0x806C # 1 F
	UNPACK_SKIP_IMAGES				= 0x806D # 1 I
	UNPACK_SKIP_IMAGES_EXT				= 0x806D # 1 I
	UNPACK_IMAGE_HEIGHT				= 0x806E # 1 F
	UNPACK_IMAGE_HEIGHT_EXT				= 0x806E # 1 F
	TEXTURE_3D					= 0x806F # 1 I
	TEXTURE_3D_EXT					= 0x806F # 1 I
	PROXY_TEXTURE_3D				= 0x8070
	PROXY_TEXTURE_3D_EXT				= 0x8070
	TEXTURE_DEPTH					= 0x8071
	TEXTURE_DEPTH_EXT				= 0x8071
	TEXTURE_WRAP_R					= 0x8072
	TEXTURE_WRAP_R_EXT				= 0x8072
	MAX_3D_TEXTURE_SIZE				= 0x8073 # 1 I
	MAX_3D_TEXTURE_SIZE_EXT				= 0x8073 # 1 I

###############################################################################

EXT_vertex_array enum:
	VERTEX_ARRAY_EXT				= 0x8074
	NORMAL_ARRAY_EXT				= 0x8075
	COLOR_ARRAY_EXT					= 0x8076
	INDEX_ARRAY_EXT					= 0x8077
	TEXTURE_COORD_ARRAY_EXT				= 0x8078
	EDGE_FLAG_ARRAY_EXT				= 0x8079
	VERTEX_ARRAY_SIZE_EXT				= 0x807A
	VERTEX_ARRAY_TYPE_EXT				= 0x807B
	VERTEX_ARRAY_STRIDE_EXT				= 0x807C
	VERTEX_ARRAY_COUNT_EXT				= 0x807D # 1 I
	NORMAL_ARRAY_TYPE_EXT				= 0x807E
	NORMAL_ARRAY_STRIDE_EXT				= 0x807F
	NORMAL_ARRAY_COUNT_EXT				= 0x8080 # 1 I
	COLOR_ARRAY_SIZE_EXT				= 0x8081
	COLOR_ARRAY_TYPE_EXT				= 0x8082
	COLOR_ARRAY_STRIDE_EXT				= 0x8083
	COLOR_ARRAY_COUNT_EXT				= 0x8084 # 1 I
	INDEX_ARRAY_TYPE_EXT				= 0x8085
	INDEX_ARRAY_STRIDE_EXT				= 0x8086
	INDEX_ARRAY_COUNT_EXT				= 0x8087 # 1 I
	TEXTURE_COORD_ARRAY_SIZE_EXT			= 0x8088
	TEXTURE_COORD_ARRAY_TYPE_EXT			= 0x8089
	TEXTURE_COORD_ARRAY_STRIDE_EXT			= 0x808A
	TEXTURE_COORD_ARRAY_COUNT_EXT			= 0x808B # 1 I
	EDGE_FLAG_ARRAY_STRIDE_EXT			= 0x808C
	EDGE_FLAG_ARRAY_COUNT_EXT			= 0x808D # 1 I
	VERTEX_ARRAY_POINTER_EXT			= 0x808E
	NORMAL_ARRAY_POINTER_EXT			= 0x808F
	COLOR_ARRAY_POINTER_EXT				= 0x8090
	INDEX_ARRAY_POINTER_EXT				= 0x8091
	TEXTURE_COORD_ARRAY_POINTER_EXT			= 0x8092
	EDGE_FLAG_ARRAY_POINTER_EXT			= 0x8093

###############################################################################

SGIX_interlace enum:
	INTERLACE_SGIX					= 0x8094 # 1 I

###############################################################################

SGIS_detail_texture enum:
	DETAIL_TEXTURE_2D_SGIS				= 0x8095
	DETAIL_TEXTURE_2D_BINDING_SGIS			= 0x8096 # 1 I
	LINEAR_DETAIL_SGIS				= 0x8097
	LINEAR_DETAIL_ALPHA_SGIS			= 0x8098
	LINEAR_DETAIL_COLOR_SGIS			= 0x8099
	DETAIL_TEXTURE_LEVEL_SGIS			= 0x809A
	DETAIL_TEXTURE_MODE_SGIS			= 0x809B
	DETAIL_TEXTURE_FUNC_POINTS_SGIS			= 0x809C

###############################################################################

SGIS_multisample enum:
	MULTISAMPLE_SGIS				= 0x809D # 1 I
	SAMPLE_ALPHA_TO_MASK_SGIS			= 0x809E # 1 I
	SAMPLE_ALPHA_TO_ONE_SGIS			= 0x809F # 1 I
	SAMPLE_MASK_SGIS				= 0x80A0 # 1 I
	1PASS_SGIS					= 0x80A1
	2PASS_0_SGIS					= 0x80A2
	2PASS_1_SGIS					= 0x80A3
	4PASS_0_SGIS					= 0x80A4
	4PASS_1_SGIS					= 0x80A5
	4PASS_2_SGIS					= 0x80A6
	4PASS_3_SGIS					= 0x80A7
	SAMPLE_BUFFERS_SGIS				= 0x80A8 # 1 I
	SAMPLES_SGIS					= 0x80A9 # 1 I
	SAMPLE_MASK_VALUE_SGIS				= 0x80AA # 1 F
	SAMPLE_MASK_INVERT_SGIS				= 0x80AB # 1 I
	SAMPLE_PATTERN_SGIS				= 0x80AC # 1 I

# Reuses SGIS_multisample values.
# EXT_multisample enum:
#	  MULTISAMPLE_EXT				  = 0x809D
#	  SAMPLE_ALPHA_TO_MASK_EXT			  = 0x809E
#	  SAMPLE_ALPHA_TO_ONE_EXT			  = 0x809F
#	  SAMPLE_MASK_EXT				  = 0x80A0
#	  1PASS_EXT					  = 0x80A1
#	  2PASS_0_EXT					  = 0x80A2
#	  2PASS_1_EXT					  = 0x80A3
#	  4PASS_0_EXT					  = 0x80A4
#	  4PASS_1_EXT					  = 0x80A5
#	  4PASS_2_EXT					  = 0x80A6
#	  4PASS_3_EXT					  = 0x80A7
#	  SAMPLE_BUFFERS_EXT				  = 0x80A8 # 1 I
#	  SAMPLES_EXT					  = 0x80A9 # 1 I
#	  SAMPLE_MASK_VALUE_EXT				  = 0x80AA # 1 F
#	  SAMPLE_MASK_INVERT_EXT			  = 0x80AB # 1 I
#	  SAMPLE_PATTERN_EXT				  = 0x80AC # 1 I

# Reuses some SGIS_multisample values
ARB_multisample enum:
	MULTISAMPLE_ARB					= 0x809D
	SAMPLE_ALPHA_TO_COVERAGE_ARB			= 0x809E
	SAMPLE_ALPHA_TO_ONE_ARB				= 0x809F
	SAMPLE_COVERAGE_ARB				= 0x80A0
	SAMPLE_BUFFERS_ARB				= 0x80A8 # 1 I
	SAMPLES_ARB					= 0x80A9 # 1 I
	SAMPLE_COVERAGE_VALUE_ARB			= 0x80AA # 1 F
	SAMPLE_COVERAGE_INVERT_ARB			= 0x80AB # 1 I

###############################################################################

SGIS_sharpen_texture enum:
	LINEAR_SHARPEN_SGIS				= 0x80AD
	LINEAR_SHARPEN_ALPHA_SGIS			= 0x80AE
	LINEAR_SHARPEN_COLOR_SGIS			= 0x80AF
	SHARPEN_TEXTURE_FUNC_POINTS_SGIS		= 0x80B0

###############################################################################

SGI_color_matrix enum:
	COLOR_MATRIX					= 0x80B1 # 16 F
	COLOR_MATRIX_SGI				= 0x80B1 # 16 F
	COLOR_MATRIX_STACK_DEPTH			= 0x80B2 # 1 I
	COLOR_MATRIX_STACK_DEPTH_SGI			= 0x80B2 # 1 I
	MAX_COLOR_MATRIX_STACK_DEPTH			= 0x80B3 # 1 I
	MAX_COLOR_MATRIX_STACK_DEPTH_SGI		= 0x80B3 # 1 I
	POST_COLOR_MATRIX_RED_SCALE			= 0x80B4 # 1 F
	POST_COLOR_MATRIX_RED_SCALE_SGI			= 0x80B4 # 1 F
	POST_COLOR_MATRIX_GREEN_SCALE			= 0x80B5 # 1 F
	POST_COLOR_MATRIX_GREEN_SCALE_SGI		= 0x80B5 # 1 F
	POST_COLOR_MATRIX_BLUE_SCALE			= 0x80B6 # 1 F
	POST_COLOR_MATRIX_BLUE_SCALE_SGI		= 0x80B6 # 1 F
	POST_COLOR_MATRIX_ALPHA_SCALE			= 0x80B7 # 1 F
	POST_COLOR_MATRIX_ALPHA_SCALE_SGI		= 0x80B7 # 1 F
	POST_COLOR_MATRIX_RED_BIAS			= 0x80B8 # 1 F
	POST_COLOR_MATRIX_RED_BIAS_SGI			= 0x80B8 # 1 F
	POST_COLOR_MATRIX_GREEN_BIAS			= 0x80B9 # 1 F
	POST_COLOR_MATRIX_GREEN_BIAS_SGI		= 0x80B9 # 1 F
	POST_COLOR_MATRIX_BLUE_BIAS			= 0x80BA # 1 F
	POST_COLOR_MATRIX_BLUE_BIAS_SGI			= 0x80BA # 1 F
	POST_COLOR_MATRIX_ALPHA_BIAS			= 0x80BB # 1 F
	POST_COLOR_MATRIX_ALPHA_BIAS_SGI		= 0x80BB # 1 F

###############################################################################

SGI_texture_color_table enum:
	TEXTURE_COLOR_TABLE_SGI				= 0x80BC # 1 I
	PROXY_TEXTURE_COLOR_TABLE_SGI			= 0x80BD

###############################################################################

SGIX_texture_add_env enum:
	TEXTURE_ENV_BIAS_SGIX				= 0x80BE

###############################################################################

SGIX_shadow_ambient enum:
	SHADOW_AMBIENT_SGIX				= 0x80BF

###############################################################################

# Intergraph: 0x80C0-0x80CF

# EXT_blend_func_separate enum:
#	BLEND_DST_RGB_EXT				= 0x80C8
#	BLEND_SRC_RGB_EXT				= 0x80C9
#	BLEND_DST_ALPHA_EXT				= 0x80CA
#	BLEND_SRC_ALPHA_EXT				= 0x80CB

# EXT_422_pixels enum:
#	422_EXT						= 0x80CC
#	422_REV_EXT					= 0x80CD
#	422_AVERAGE_EXT					= 0x80CE
#	422_REV_AVERAGE_EXT				= 0x80CF

###############################################################################

SGI_color_table enum:
	COLOR_TABLE					= 0x80D0 # 1 I
	COLOR_TABLE_SGI					= 0x80D0 # 1 I
	POST_CONVOLUTION_COLOR_TABLE			= 0x80D1 # 1 I
	POST_CONVOLUTION_COLOR_TABLE_SGI		= 0x80D1 # 1 I
	POST_COLOR_MATRIX_COLOR_TABLE			= 0x80D2 # 1 I
	POST_COLOR_MATRIX_COLOR_TABLE_SGI		= 0x80D2 # 1 I
	PROXY_COLOR_TABLE				= 0x80D3
	PROXY_COLOR_TABLE_SGI				= 0x80D3
	PROXY_POST_CONVOLUTION_COLOR_TABLE		= 0x80D4
	PROXY_POST_CONVOLUTION_COLOR_TABLE_SGI		= 0x80D4
	PROXY_POST_COLOR_MATRIX_COLOR_TABLE		= 0x80D5
	PROXY_POST_COLOR_MATRIX_COLOR_TABLE_SGI		= 0x80D5
	COLOR_TABLE_SCALE				= 0x80D6
	COLOR_TABLE_SCALE_SGI				= 0x80D6
	COLOR_TABLE_BIAS				= 0x80D7
	COLOR_TABLE_BIAS_SGI				= 0x80D7
	COLOR_TABLE_FORMAT				= 0x80D8
	COLOR_TABLE_FORMAT_SGI				= 0x80D8
	COLOR_TABLE_WIDTH				= 0x80D9
	COLOR_TABLE_WIDTH_SGI				= 0x80D9
	COLOR_TABLE_RED_SIZE				= 0x80DA
	COLOR_TABLE_RED_SIZE_SGI			= 0x80DA
	COLOR_TABLE_GREEN_SIZE				= 0x80DB
	COLOR_TABLE_GREEN_SIZE_SGI			= 0x80DB
	COLOR_TABLE_BLUE_SIZE				= 0x80DC
	COLOR_TABLE_BLUE_SIZE_SGI			= 0x80DC
	COLOR_TABLE_ALPHA_SIZE				= 0x80DD
	COLOR_TABLE_ALPHA_SIZE_SGI			= 0x80DD
	COLOR_TABLE_LUMINANCE_SIZE			= 0x80DE
	COLOR_TABLE_LUMINANCE_SIZE_SGI			= 0x80DE
	COLOR_TABLE_INTENSITY_SIZE			= 0x80DF
	COLOR_TABLE_INTENSITY_SIZE_SGI			= 0x80DF

###############################################################################

VERSION_1_2 enum:
	BGR						= 0x80E0
	BGRA						= 0x80E1

###############################################################################

# Microsoft: 0x80E2-0x80E7

###############################################################################

VERSION_1_2 enum:
	MAX_ELEMENTS_VERTICES				= 0x80E8
	MAX_ELEMENTS_INDICES				= 0x80E9

###############################################################################

# Microsoft: 0x80EA-0x810F

###############################################################################

SGIS_texture_select enum:
	DUAL_ALPHA4_SGIS				= 0x8110
	DUAL_ALPHA8_SGIS				= 0x8111
	DUAL_ALPHA12_SGIS				= 0x8112
	DUAL_ALPHA16_SGIS				= 0x8113
	DUAL_LUMINANCE4_SGIS				= 0x8114
	DUAL_LUMINANCE8_SGIS				= 0x8115
	DUAL_LUMINANCE12_SGIS				= 0x8116
	DUAL_LUMINANCE16_SGIS				= 0x8117
	DUAL_INTENSITY4_SGIS				= 0x8118
	DUAL_INTENSITY8_SGIS				= 0x8119
	DUAL_INTENSITY12_SGIS				= 0x811A
	DUAL_INTENSITY16_SGIS				= 0x811B
	DUAL_LUMINANCE_ALPHA4_SGIS			= 0x811C
	DUAL_LUMINANCE_ALPHA8_SGIS			= 0x811D
	QUAD_ALPHA4_SGIS				= 0x811E
	QUAD_ALPHA8_SGIS				= 0x811F
	QUAD_LUMINANCE4_SGIS				= 0x8120
	QUAD_LUMINANCE8_SGIS				= 0x8121
	QUAD_INTENSITY4_SGIS				= 0x8122
	QUAD_INTENSITY8_SGIS				= 0x8123
	DUAL_TEXTURE_SELECT_SGIS			= 0x8124
	QUAD_TEXTURE_SELECT_SGIS			= 0x8125

###############################################################################

SGIS_point_parameters enum:
	POINT_SIZE_MIN_EXT				= 0x8126 # 1 F
	POINT_SIZE_MIN_SGIS				= 0x8126 # 1 F
	POINT_SIZE_MAX_EXT				= 0x8127 # 1 F
	POINT_SIZE_MAX_SGIS				= 0x8127 # 1 F
	POINT_FADE_THRESHOLD_SIZE_EXT			= 0x8128 # 1 F
	POINT_FADE_THRESHOLD_SIZE_SGIS			= 0x8128 # 1 F
	DISTANCE_ATTENUATION_EXT			= 0x8129 # 3 F
	DISTANCE_ATTENUATION_SGIS			= 0x8129 # 3 F

###############################################################################

SGIS_fog_function enum:
	FOG_FUNC_SGIS					= 0x812A
	FOG_FUNC_POINTS_SGIS				= 0x812B # 1 I
	MAX_FOG_FUNC_POINTS_SGIS			= 0x812C # 1 I

###############################################################################

SGIS_texture_border_clamp enum:
	CLAMP_TO_BORDER_SGIS				= 0x812D

###############################################################################

SGIX_texture_multi_buffer enum:
	TEXTURE_MULTI_BUFFER_HINT_SGIX			= 0x812E

###############################################################################

SGIS_texture_edge_clamp enum:
	CLAMP_TO_EDGE					= 0x812F
	CLAMP_TO_EDGE_SGIS				= 0x812F

###############################################################################

SGIS_texture4D enum:
	PACK_SKIP_VOLUMES_SGIS				= 0x8130 # 1 I
	PACK_IMAGE_DEPTH_SGIS				= 0x8131 # 1 I
	UNPACK_SKIP_VOLUMES_SGIS			= 0x8132 # 1 I
	UNPACK_IMAGE_DEPTH_SGIS				= 0x8133 # 1 I
	TEXTURE_4D_SGIS					= 0x8134 # 1 I
	PROXY_TEXTURE_4D_SGIS				= 0x8135
	TEXTURE_4DSIZE_SGIS				= 0x8136
	TEXTURE_WRAP_Q_SGIS				= 0x8137
	MAX_4D_TEXTURE_SIZE_SGIS			= 0x8138 # 1 I
	TEXTURE_4D_BINDING_SGIS				= 0x814F # 1 I

###############################################################################

SGIX_pixel_texture enum:
	PIXEL_TEX_GEN_SGIX				= 0x8139 # 1 I
	PIXEL_TEX_GEN_MODE_SGIX				= 0x832B # 1 I

###############################################################################

SGIS_texture_lod enum:
	TEXTURE_MIN_LOD					= 0x813A
	TEXTURE_MIN_LOD_SGIS				= 0x813A
	TEXTURE_MAX_LOD					= 0x813B
	TEXTURE_MAX_LOD_SGIS				= 0x813B
	TEXTURE_BASE_LEVEL				= 0x813C
	TEXTURE_BASE_LEVEL_SGIS				= 0x813C
	TEXTURE_MAX_LEVEL				= 0x813D
	TEXTURE_MAX_LEVEL_SGIS				= 0x813D

###############################################################################

SGIX_pixel_tiles enum:
	PIXEL_TILE_BEST_ALIGNMENT_SGIX			= 0x813E # 1 I
	PIXEL_TILE_CACHE_INCREMENT_SGIX			= 0x813F # 1 I
	PIXEL_TILE_WIDTH_SGIX				= 0x8140 # 1 I
	PIXEL_TILE_HEIGHT_SGIX				= 0x8141 # 1 I
	PIXEL_TILE_GRID_WIDTH_SGIX			= 0x8142 # 1 I

	PIXEL_TILE_GRID_HEIGHT_SGIX			= 0x8143 # 1 I
	PIXEL_TILE_GRID_DEPTH_SGIX			= 0x8144 # 1 I
	PIXEL_TILE_CACHE_SIZE_SGIX			= 0x8145 # 1 I

###############################################################################

SGIS_texture_filter4 enum:
	FILTER4_SGIS					= 0x8146
	TEXTURE_FILTER4_SIZE_SGIS			= 0x8147

###############################################################################

SGIX_sprite enum:
	SPRITE_SGIX					= 0x8148 # 1 I
	SPRITE_MODE_SGIX				= 0x8149 # 1 I
	SPRITE_AXIS_SGIX				= 0x814A # 3 F
	SPRITE_TRANSLATION_SGIX				= 0x814B # 3 F
	SPRITE_AXIAL_SGIX				= 0x814C
	SPRITE_OBJECT_ALIGNED_SGIX			= 0x814D
	SPRITE_EYE_ALIGNED_SGIX				= 0x814E

###############################################################################

# SGIS_texture4D (additional; see above): 0x814F

###############################################################################

VERSION_1_2 enum:
	IGNORE_BORDER					= 0x8150
	CONSTANT_BORDER					= 0x8151
	WRAP_BORDER					= 0x8152
	REPLICATE_BORDER				= 0x8153
	CONVOLUTION_BORDER_COLOR			= 0x8154

###############################################################################

# HP: 0x8155-0x816F

###############################################################################

SGIX_clipmap enum:
	LINEAR_CLIPMAP_LINEAR_SGIX			= 0x8170
	TEXTURE_CLIPMAP_CENTER_SGIX			= 0x8171
	TEXTURE_CLIPMAP_FRAME_SGIX			= 0x8172
	TEXTURE_CLIPMAP_OFFSET_SGIX			= 0x8173
	TEXTURE_CLIPMAP_VIRTUAL_DEPTH_SGIX		= 0x8174
	TEXTURE_CLIPMAP_LOD_OFFSET_SGIX			= 0x8175
	TEXTURE_CLIPMAP_DEPTH_SGIX			= 0x8176
	MAX_CLIPMAP_DEPTH_SGIX				= 0x8177 # 1 I
	MAX_CLIPMAP_VIRTUAL_DEPTH_SGIX			= 0x8178 # 1 I
	NEAREST_CLIPMAP_NEAREST_SGIX			= 0x844D
	NEAREST_CLIPMAP_LINEAR_SGIX			= 0x844E
	LINEAR_CLIPMAP_NEAREST_SGIX			= 0x844F

###############################################################################

SGIX_texture_scale_bias enum:
	POST_TEXTURE_FILTER_BIAS_SGIX			= 0x8179
	POST_TEXTURE_FILTER_SCALE_SGIX			= 0x817A
	POST_TEXTURE_FILTER_BIAS_RANGE_SGIX		= 0x817B # 2 F
	POST_TEXTURE_FILTER_SCALE_RANGE_SGIX		= 0x817C # 2 F

###############################################################################

SGIX_reference_plane enum:
	REFERENCE_PLANE_SGIX				= 0x817D # 1 I
	REFERENCE_PLANE_EQUATION_SGIX			= 0x817E # 4 F

###############################################################################

SGIX_ir_instrument1 enum:
	IR_INSTRUMENT1_SGIX				= 0x817F # 1 I

###############################################################################

SGIX_instruments enum:
	INSTRUMENT_BUFFER_POINTER_SGIX			= 0x8180
	INSTRUMENT_MEASUREMENTS_SGIX			= 0x8181 # 1 I

###############################################################################

SGIX_list_priority enum:
	LIST_PRIORITY_SGIX				= 0x8182

###############################################################################

SGIX_calligraphic_fragment enum:
	CALLIGRAPHIC_FRAGMENT_SGIX			= 0x8183 # 1 I

###############################################################################

SGIX_impact_pixel_texture enum:
	PIXEL_TEX_GEN_Q_CEILING_SGIX			= 0x8184
	PIXEL_TEX_GEN_Q_ROUND_SGIX			= 0x8185
	PIXEL_TEX_GEN_Q_FLOOR_SGIX			= 0x8186
	PIXEL_TEX_GEN_ALPHA_REPLACE_SGIX		= 0x8187
	PIXEL_TEX_GEN_ALPHA_NO_REPLACE_SGIX		= 0x8188
	PIXEL_TEX_GEN_ALPHA_LS_SGIX			= 0x8189
	PIXEL_TEX_GEN_ALPHA_MS_SGIX			= 0x818A

###############################################################################

SGIX_framezoom enum:
	FRAMEZOOM_SGIX					= 0x818B # 1 I
	FRAMEZOOM_FACTOR_SGIX				= 0x818C # 1 I
	MAX_FRAMEZOOM_FACTOR_SGIX			= 0x818D # 1 I

###############################################################################

SGIX_texture_lod_bias enum:
	TEXTURE_LOD_BIAS_S_SGIX				= 0x818E
	TEXTURE_LOD_BIAS_T_SGIX				= 0x818F
	TEXTURE_LOD_BIAS_R_SGIX				= 0x8190

###############################################################################

SGIS_generate_mipmap enum:
	GENERATE_MIPMAP_SGIS				= 0x8191
	GENERATE_MIPMAP_HINT_SGIS			= 0x8192 # 1 I

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_spotlight_cutoff: 0x8193
#	SPOT_CUTOFF_DELTA_SGIX				= 0x8193

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_polynomial_ffd enum:
#	GEOMETRY_DEFORMATION_SGIX			= 0x8194
#	TEXTURE_DEFORMATION_SGIX			= 0x8195
#	DEFORMATIONS_MASK_SGIX				= 0x8196 # 1 I
#	MAX_DEFORMATION_ORDER_SGIX			= 0x8197

###############################################################################

SGIX_fog_offset enum:
	FOG_OFFSET_SGIX					= 0x8198 # 1 I
	FOG_OFFSET_VALUE_SGIX				= 0x8199 # 4 F

###############################################################################

SGIX_shadow enum:
	TEXTURE_COMPARE_SGIX				= 0x819A
	TEXTURE_COMPARE_OPERATOR_SGIX			= 0x819B
	TEXTURE_LEQUAL_R_SGIX				= 0x819C
	TEXTURE_GEQUAL_R_SGIX				= 0x819D

###############################################################################

# SGI private extension, not in enumext.spec
# SGIX_igloo_interface: 0x819E-0x81A4
#	IGLOO_FULLSCREEN_SGIX				= 0x819E
#	IGLOO_VIEWPORT_OFFSET_SGIX			= 0x819F
#	IGLOO_SWAPTMESH_SGIX				= 0x81A0
#	IGLOO_COLORNORMAL_SGIX				= 0x81A1
#	IGLOO_IRISGL_MODE_SGIX				= 0x81A2
#	IGLOO_LMC_COLOR_SGIX				= 0x81A3
#	IGLOO_TMESHMODE_SGIX				= 0x81A4

###############################################################################

SGIX_depth_texture enum:
	DEPTH_COMPONENT16_SGIX				= 0x81A5
	DEPTH_COMPONENT24_SGIX				= 0x81A6
	DEPTH_COMPONENT32_SGIX				= 0x81A7

###############################################################################

#EXT_compiled_vertex_array enum:
#	 ARRAY_ELEMENT_LOCK_FIRST_EXT			 = 0x81A8
#	 ARRAY_ELEMENT_LOCK_COUNT_EXT			 = 0x81A9

###############################################################################

#EXT_cull_vertex enum:
#	 CULL_VERTEX_EXT				 = 0x81AA
#	 CULL_VERTEX_EYE_POSITION_EXT			 = 0x81AB
#	 CULL_VERTEX_OBJECT_POSITION_EXT		 = 0x81AC

###############################################################################

# Promoted from SGI?
#EXT_index_array_formats enum:
#	 IUI_V2F_EXT					 = 0x81AD
#	 IUI_V3F_EXT					 = 0x81AE
#	 IUI_N3F_V2F_EXT				 = 0x81AF
#	 IUI_N3F_V3F_EXT				 = 0x81B0
#	 T2F_IUI_V2F_EXT				 = 0x81B1
#	 T2F_IUI_V3F_EXT				 = 0x81B2
#	 T2F_IUI_N3F_V2F_EXT				 = 0x81B3
#	 T2F_IUI_N3F_V3F_EXT				 = 0x81B4

###############################################################################

# Promoted from SGI?
#EXT_index_func enum:
#	 INDEX_TEST_EXT					 = 0x81B5
#	 INDEX_TEST_FUNC_EXT				 = 0x81B6
#	 INDEX_TEST_REF_EXT				 = 0x81B7

###############################################################################

# Promoted from SGI?
#EXT_index_material enum:
#	 INDEX_MATERIAL_EXT				 = 0x81B8
#	 INDEX_MATERIAL_PARAMETER_EXT			 = 0x81B9
#	 INDEX_MATERIAL_FACE_EXT			 = 0x81BA

###############################################################################

SGIX_ycrcb enum:
	YCRCB_422_SGIX					= 0x81BB
	YCRCB_444_SGIX					= 0x81BC

###############################################################################

# Incomplete extension, not in enumext.spec
# SGI_complex_type: 0x81BD-0x81C3
#	COMPLEX_UNSIGNED_BYTE_SGI			= 0x81BD
#	COMPLEX_BYTE_SGI				= 0x81BE
#	COMPLEX_UNSIGNED_SHORT_SGI			= 0x81BF
#	COMPLEX_SHORT_SGI				= 0x81C0
#	COMPLEX_UNSIGNED_INT_SGI			= 0x81C1
#	COMPLEX_INT_SGI					= 0x81C2
#	COMPLEX_FLOAT_SGI				= 0x81C3

###############################################################################

# Incomplete extension, not in enumext.spec
# SGI_fft: 0x81C4-0x81CA
#	POST_TRANSFORM_RED_SCALE_SGI			= ????	 # 1 F
#	POST_TRANSFORM_GREEN_SCALE_SGI			= ????	 # 1 F
#	POST_TRANSFORM_BLUE_SCALE_SGI			= ????	 # 1 F
#	POST_TRANSFORM_ALPHA_SCALE_SGI			= ????	 # 1 F
#	POST_TRANSFORM_RED_BIAS_SGI			= ????	 # 1 F
#	POST_TRANSFORM_GREEN_BIAS_SGI			= ????	 # 1 F
#	POST_TRANSFORM_BLUE_BIAS_SGI			= ????	 # 1 F
#	POST_TRANSFORM_ALPHA_BIAS_SGI			= ????	 # 1 F
#	PIXEL_TRANSFORM_OPERATOR_SGI			= 0x81C4 # 1 I
#	CONVOLUTION_SGI					= 0x81C5
#	FFT_1D_SGI					= 0x81C6
#	PIXEL_TRANSFORM_SGI				= 0x81C7
#	MAX_FFT_WIDTH_SGI				= 0x81C8
#	SORT_SGI					= 0x81C9
#	TRANSPOSE_SGI					= 0x81CA

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_nurbs_eval: 0x81CB-0x81CF
#	MAP1_VERTEX_3_NURBS_SGIX			= 0x81CB # 1 I
#	MAP1_VERTEX_4_NURBS_SGIX			= 0x81CC # 1 I
#	MAP1_INDEX_NURBS_SGIX				= 0x81CD # 1 I
#	MAP1_COLOR_4_NURBS_SGIX				= 0x81CE # 1 I
#	MAP1_NORMAL_NURBS_SGIX				= 0x81CF # 1 I
#	MAP1_TEXTURE_COORD_1_NURBS_SGIX			= 0x81E0 # 1 I
#	MAP1_TEXTURE_COORD_2_NURBS_SGIX			= 0x81E1 # 1 I
#	MAP1_TEXTURE_COORD_3_NURBS_SGIX			= 0x81E2 # 1 I
#	MAP1_TEXTURE_COORD_4_NURBS_SGIX			= 0x81E3 # 1 I
#	MAP2_VERTEX_3_NURBS_SGIX			= 0x81E4 # 1 I
#	MAP2_VERTEX_4_NURBS_SGIX			= 0x81E5 # 1 I
#	MAP2_INDEX_NURBS_SGIX				= 0x81E6 # 1 I
#	MAP2_COLOR_4_NURBS_SGIX				= 0x81E7 # 1 I
#	MAP2_NORMAL_NURBS_SGIX				= 0x81E8 # 1 I
#	MAP2_TEXTURE_COORD_1_NURBS_SGIX			= 0x81E9 # 1 I
#	MAP2_TEXTURE_COORD_2_NURBS_SGIX			= 0x81EA # 1 I
#	MAP2_TEXTURE_COORD_3_NURBS_SGIX			= 0x81EB # 1 I
#	MAP2_TEXTURE_COORD_4_NURBS_SGIX			= 0x81EC # 1 I
#	NURBS_KNOT_COUNT_SGIX				= 0x81ED
#	NURBS_KNOT_VECTOR_SGIX				= 0x81EE

###############################################################################

# Sun: 0x81D0-0x81DF

# No extension spec, not in enumext.spec
# SUNX_surface_hint enum:
#	 SURFACE_SIZE_HINT_SUNX				= 0x81D2
#	 LARGE_SUNX					= 0x81D3

# SUNX_general_triangle_list enum:
#	 RESTART_SUN					= 0x01
#	 REPLACE_MIDDLE_SUN				= 0x02
#	 REPLACE_OLDEST_SUN				= 0x03
#	 WRAP_BORDER_SUN				= 0x81D4
#	 TRIANGLE_LIST_SUN				= 0x81D7
#	 REPLACEMENT_CODE_SUN				= 0x81D8
#	 REPLACEMENT_CODE_ARRAY_SUN			= 0x85C0
#	 REPLACEMENT_CODE_ARRAY_TYPE_SUN		= 0x85C1
#	 REPLACEMENT_CODE_ARRAY_STRIDE_SUN		= 0x85C2
#	 REPLACEMENT_CODE_ARRAY_POINTER_SUN		= 0x85C3
#	 R1UI_V3F_SUN					= 0x85C4
#	 R1UI_C4UB_V3F_SUN				= 0x85C5
#	 R1UI_C3F_V3F_SUN				= 0x85C6
#	 R1UI_N3F_V3F_SUN				= 0x85C7
#	 R1UI_C4F_N3F_V3F_SUN				= 0x85C8
#	 R1UI_T2F_V3F_SUN				= 0x85C9
#	 R1UI_T2F_N3F_V3F_SUN				= 0x85CA
#	 R1UI_T2F_C4F_N3F_V3F_SUN			= 0x85CB

# SUNX_constant_data enum:
#	 UNPACK_CONSTANT_DATA_SUNX			= 0x81D5
#	 TEXTURE_CONSTANT_DATA_SUNX			= 0x81D6

# SUN_global_alpha enum:
#	 GLOBAL_ALPHA_SUN				= 0x81D9
#	 GLOBAL_ALPHA_FACTOR_SUN			= 0x81DA

###############################################################################

# SGIX_nurbs_eval (additional; see above): 0x81E0-0x81EE

###############################################################################

SGIS_texture_color_mask enum:
	TEXTURE_COLOR_WRITEMASK_SGIS			= 0x81EF

###############################################################################

SGIS_point_line_texgen enum:
	EYE_DISTANCE_TO_POINT_SGIS			= 0x81F0
	OBJECT_DISTANCE_TO_POINT_SGIS			= 0x81F1
	EYE_DISTANCE_TO_LINE_SGIS			= 0x81F2
	OBJECT_DISTANCE_TO_LINE_SGIS			= 0x81F3
	EYE_POINT_SGIS					= 0x81F4
	OBJECT_POINT_SGIS				= 0x81F5
	EYE_LINE_SGIS					= 0x81F6
	OBJECT_LINE_SGIS				= 0x81F7

###############################################################################

VERSION_1_2 enum:
	LIGHT_MODEL_COLOR_CONTROL			= 0x81F8 # 1 I
	SINGLE_COLOR					= 0x81F9
	SEPARATE_SPECULAR_COLOR				= 0x81FA

###############################################################################

EXT_shared_texture_palette enum:
	SHARED_TEXTURE_PALETTE_EXT			= 0x81FB # 1 I

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_fog_scale: 0x81FC-0x81FD
#	FOG_SCALE_SGIX					= 0x81FC # 1 I
#	FOG_SCALE_VALUE_SGIX				= 0x81FD # 1 F

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_fog_blend: 0x81FE-0x81FF
#	FOG_BLEND_ALPHA_SGIX				= 0x81FE # 1 I
#	FOG_BLEND_COLOR_SGIX				= 0x81FF # 1 I

###############################################################################

# Microsoft: 0x8200-0x82AF

###############################################################################

# ADD: 0x82B0-0x830F

###############################################################################

# SGIX_depth_pass_instrument enum: 0x8310-0x8312
#	DEPTH_PASS_INSTRUMENT_SGIX			= 0x8310
#	DEPTH_PASS_INSTRUMENT_COUNTERS_SGIX		= 0x8311
#	DEPTH_PASS_INSTRUMENT_MAX_SGIX			= 0x8312

###############################################################################

# SGIX_fragments_instrument enum: 0x8313-0x8315
#	FRAGMENTS_INSTRUMENT_SGIX			= 0x8313 # 1 I
#	FRAGMENTS_INSTRUMENT_COUNTERS_SGIX		= 0x8314 # 1 I
#	FRAGMENTS_INSTRUMENT_MAX_SGIX			= 0x8315 # 1 I

###############################################################################

SGIX_convolution_accuracy enum:
	CONVOLUTION_HINT_SGIX				= 0x8316 # 1 I

###############################################################################

# SGIX_color_matrix_accuracy: 0x8317

###############################################################################

# SGIX_ycrcba: 0x8318-0x8319
#	YCRCB_SGIX					= 0x8318
#	YCRCBA_SGIX					= 0x8319

###############################################################################

# SGIX_slim: 0x831A-0x831F
#	UNPACK_COMPRESSED_SIZE_SGIX			= 0x831A
#	PACK_MAX_COMPRESSED_SIZE_SGIX			= 0x831B
#	PACK_COMPRESSED_SIZE_SGIX			= 0x831C
#	SLIM8U_SGIX					= 0x831D
#	SLIM10U_SGIX					= 0x831E
#	SLIM12S_SGIX					= 0x831F

###############################################################################

SGIX_blend_alpha_minmax enum:
	ALPHA_MIN_SGIX					= 0x8320
	ALPHA_MAX_SGIX					= 0x8321

###############################################################################

# SGI_future_use: 0x8322

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_fog_layers: 0x8323-0x8328
#	FOG_TYPE_SGIX					= 0x8323 # 1 I
#	UNIFORM_SGIX					= 0x8324
#	LAYERED_SGIX					= 0x8325
#	FOG_GROUND_PLANE_SGIX				= 0x8326 # 4 F
#	FOG_LAYERS_POINTS_SGIX				= 0x8327 # 1 I
#	MAX_FOG_LAYERS_POINTS_SGIX			= 0x8328 # 1 I

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_async enum:
#	ASYNC_MARKER_SGIX				= 0x8329

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_texture_phase: 0x832A
#	PHASE_SGIX					= 0x832A

###############################################################################

# SGIX_pixel_texture (additional; see above): 0x832B

###############################################################################

# Incomplete extension, not in enumext.spec
SGIX_async_histogram enum:
	ASYNC_HISTOGRAM_SGIX				= 0x832C
	MAX_ASYNC_HISTOGRAM_SGIX			= 0x832D

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_texture_mipmap_anisotropic: 0x832E-0x832F
#	TEXTURE_MIPMAP_ANISOTROPY_SGIX			= 0x832E
#	MAX_MIPMAP_ANISOTROPY_SGIX			= 0x832F # 1 I

###############################################################################

EXT_pixel_transform enum:
	PIXEL_TRANSFORM_2D_EXT				= 0x8330
	PIXEL_MAG_FILTER_EXT				= 0x8331
	PIXEL_MIN_FILTER_EXT				= 0x8332
	PIXEL_CUBIC_WEIGHT_EXT				= 0x8333
	CUBIC_EXT					= 0x8334
	AVERAGE_EXT					= 0x8335
	PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT		= 0x8336
	MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT		= 0x8337
	PIXEL_TRANSFORM_2D_MATRIX_EXT			= 0x8338

# SUN_future_use: 0x8339-0x833F

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_cube_map: 0x8340-0x8348
#	ENV_MAP_SGIX					= 0x8340
#	CUBE_MAP_SGIX					= 0x8341
#	CUBE_MAP_ZP_SGIX				= 0x8342
#	CUBE_MAP_ZN_SGIX				= 0x8343
#	CUBE_MAP_XN_SGIX				= 0x8344
#	CUBE_MAP_XP_SGIX				= 0x8345
#	CUBE_MAP_YN_SGIX				= 0x8346
#	CUBE_MAP_YP_SGIX				= 0x8347
#	CUBE_MAP_BINDING_SGIX				= 0x8348 # 1 I

###############################################################################

# Unfortunately, there was a collision promoting to EXT from SGIX.
# Use fog_coord's value of 0x8452 instead of the previously
#   assigned FRAGMENT_DEPTH_EXT = 0x834B.
# EXT_light_texture: 0x8349-0x8352
#	FRAGMENT_MATERIAL_EXT				= 0x8349
#	FRAGMENT_NORMAL_EXT				= 0x834A
#	FRAGMENT_COLOR_EXT				= 0x834C
#	ATTENUATION_EXT					= 0x834D
#	SHADOW_ATTENUATION_EXT				= 0x834E
#	TEXTURE_APPLICATION_MODE_EXT			= 0x834F # 1 I
#	TEXTURE_LIGHT_EXT				= 0x8350 # 1 I
#	TEXTURE_MATERIAL_FACE_EXT			= 0x8351 # 1 I
#	TEXTURE_MATERIAL_PARAMETER_EXT			= 0x8352 # 1 I
#	use EXT_fog_coord FRAGMENT_DEPTH_EXT

###############################################################################

SGIS_pixel_texture enum:
	PIXEL_TEXTURE_SGIS				= 0x8353 # 1 I
	PIXEL_FRAGMENT_RGB_SOURCE_SGIS			= 0x8354 # 1 I
	PIXEL_FRAGMENT_ALPHA_SOURCE_SGIS		= 0x8355 # 1 I
	PIXEL_GROUP_COLOR_SGIS				= 0x8356 # 1 I

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_pixel_texture_bits: 0x8357-0x8359
#	COLOR_TO_TEXTURE_COORD_SGIX			= 0x8357
#	COLOR_BIT_PATTERN_SGIX				= 0x8358
#	COLOR_VALUE_SGIX				= 0x8359

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_pixel_texture_lod: 0x835A
#	PIXEL_TEX_GEN_LAMBDA_SOURCE_SGIX		= 0x835A

###############################################################################

# SGI_future_use: 0x835B

###############################################################################

# Incomplete extension, not in enumext.spec
SGIX_async_pixel enum:
	ASYNC_TEX_IMAGE_SGIX				= 0x835C
	ASYNC_DRAW_PIXELS_SGIX				= 0x835D
	ASYNC_READ_PIXELS_SGIX				= 0x835E
	MAX_ASYNC_TEX_IMAGE_SGIX			= 0x835F
	MAX_ASYNC_DRAW_PIXELS_SGIX			= 0x8360
	MAX_ASYNC_READ_PIXELS_SGIX			= 0x8361

###############################################################################

# EXT_packed_pixels (additional; see above): 0x8362-0x8368

###############################################################################

SGIX_texture_coordinate_clamp enum:
	TEXTURE_MAX_CLAMP_S_SGIX			= 0x8369
	TEXTURE_MAX_CLAMP_T_SGIX			= 0x836A
	TEXTURE_MAX_CLAMP_R_SGIX			= 0x836B

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_fog_texture: 0x836C-0x836E
#	FRAGMENT_FOG_SGIX				= 0x836C
#	TEXTURE_FOG_SGIX				= 0x836D # 1 I
#	FOG_PATCHY_FACTOR_SGIX				= 0x836E

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_fog_factor_to_alpha: 0x836F
	FOG_FACTOR_TO_ALPHA_SGIX			= 0x836F

###############################################################################

# HP: 0x8370-0x837F

###############################################################################

# IBM: 0x8380-0x839F

###############################################################################

# S3: 0x83A0-0x83BF

###############################################################################

# Obsolete extension, never to be put in enumext.spec
# SGIS_multitexture: 0x83C0-0x83E5
#	SELECTED_TEXTURE_SGIS				= 0x83C0 # 1 I
#	SELECTED_TEXTURE_COORD_SET_SGIS			= 0x83C1 # 1 I
#	SELECTED_TEXTURE_TRANSFORM_SGIS			= 0x83C2 # 1 I
#	MAX_TEXTURES_SGIS				= 0x83C3 # 1 I
#	MAX_TEXTURE_COORD_SETS_SGIS			= 0x83C4 # 1 I
#	TEXTURE_COORD_SET_INTERLEAVE_FACTOR_SGIS	= 0x83C5 # 1 I
#	TEXTURE_ENV_COORD_SET_SGIS			= 0x83C6
#	TEXTURE0_SGIS					= 0x83C7
#	TEXTURE1_SGIS					= 0x83C8
#	TEXTURE2_SGIS					= 0x83C9
#	TEXTURE3_SGIS					= 0x83CA
#
# SGIS_multitexture_future_use: 0x83CB-0x83E5

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_bali_g_instruments: 0x83E6-0x83E9
#	BALI_NUM_TRIS_CULLED_INSTRUMENT_SGIX		= 0x83E6 # 1 I
#	BALI_NUM_PRIMS_CLIPPED_INSTRUMENT_SGIX		= 0x83E7 # 1 I
#	BALI_NUM_PRIMS_REJECT_INSTRUMENT_SGIX		= 0x83E8 # 1 I
#	BALI_NUM_PRIMS_CLIP_RESULT_INSTRUMENT_SGIX	= 0x83E9 # 1 I

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_bali_r_instruments: 0x83EA-0x83EC
#	BALI_FRAGMENTS_GENERATED_INSTRUMENT_SGIX	= 0x83EA # 1 I
#	BALI_DEPTH_PASS_INSTRUMENT_SGIX			= 0x83EB # 1 I
#	BALI_R_CHIP_COUNT_SGIX				= 0x83EC # 1 I

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_occlusion_instrument: 0x83ED
#	OCCLUSION_INSTRUMENT_SGIX			= 0x83ED # 1 I

###############################################################################

SGIX_vertex_preclip enum:
	VERTEX_PRECLIP_SGIX				= 0x83EE
	VERTEX_PRECLIP_HINT_SGIX			= 0x83EF

###############################################################################

# INTEL: 0x83F0-0x83FF
# Note that this block was reclaimed from NTP, who never shipped it,
#   and reassigned to Intel.

EXT_texture_compression_s3tc enum:
	COMPRESSED_RGB_S3TC_DXT1_EXT			= 0x83F0
	COMPRESSED_RGBA_S3TC_DXT1_EXT			= 0x83F1
	COMPRESSED_RGBA_S3TC_DXT3_EXT			= 0x83F2
	COMPRESSED_RGBA_S3TC_DXT5_EXT			= 0x83F3

INTEL_parallel_arrays enum:
	PARALLEL_ARRAYS_INTEL				= 0x83F4
	VERTEX_ARRAY_PARALLEL_POINTERS_INTEL		= 0x83F5
	NORMAL_ARRAY_PARALLEL_POINTERS_INTEL		= 0x83F6
	COLOR_ARRAY_PARALLEL_POINTERS_INTEL		= 0x83F7
	TEXTURE_COORD_ARRAY_PARALLEL_POINTERS_INTEL	= 0x83F8

# INTEL_future_use: 0x83F9-0x83FF

###############################################################################

SGIX_fragment_lighting enum:
	FRAGMENT_LIGHTING_SGIX				= 0x8400 # 1 I
	FRAGMENT_COLOR_MATERIAL_SGIX			= 0x8401 # 1 I
	FRAGMENT_COLOR_MATERIAL_FACE_SGIX		= 0x8402 # 1 I
	FRAGMENT_COLOR_MATERIAL_PARAMETER_SGIX		= 0x8403 # 1 I
	MAX_FRAGMENT_LIGHTS_SGIX			= 0x8404 # 1 I
	MAX_ACTIVE_LIGHTS_SGIX				= 0x8405 # 1 I
	CURRENT_RASTER_NORMAL_SGIX			= 0x8406 # 1 I
	LIGHT_ENV_MODE_SGIX				= 0x8407 # 1 I
	FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_SGIX		= 0x8408 # 1 I
	FRAGMENT_LIGHT_MODEL_TWO_SIDE_SGIX		= 0x8409 # 1 I
	FRAGMENT_LIGHT_MODEL_AMBIENT_SGIX		= 0x840A # 4 F
	FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_SGIX	= 0x840B # 1 I
	FRAGMENT_LIGHT0_SGIX				= 0x840C # 1 I
	FRAGMENT_LIGHT1_SGIX				= 0x840D
	FRAGMENT_LIGHT2_SGIX				= 0x840E
	FRAGMENT_LIGHT3_SGIX				= 0x840F
	FRAGMENT_LIGHT4_SGIX				= 0x8410
	FRAGMENT_LIGHT5_SGIX				= 0x8411
	FRAGMENT_LIGHT6_SGIX				= 0x8412
	FRAGMENT_LIGHT7_SGIX				= 0x8413

# SGIX_fragment_lighting_future_use: 0x8414-0x842B

###############################################################################

SGIX_resample enum:
	PACK_RESAMPLE_SGIX				= 0x842C
	UNPACK_RESAMPLE_SGIX				= 0x842D
	RESAMPLE_REPLICATE_SGIX				= 0x842E
	RESAMPLE_ZERO_FILL_SGIX				= 0x842F
	RESAMPLE_DECIMATE_SGIX				= 0x8430

# SGIX_resample_future_use: 0x8431-0x8435

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_fragment_lighting_space: 0x8436-0x8449
#	EYE_SPACE_SGIX					= 0x8436
#	TANGENT_SPACE_SGIX				= 0x8437
#	OBJECT_SPACE_SGIX				= 0x8438
#	TANGENT_ARRAY_SGIX				= 0x8439
#	BINORMAL_ARRAY_SGIX				= 0x843A
#	CURRENT_TANGENT_SGIX				= 0x843B # 3 F
#	CURRENT_BINORMAL_SGIX				= 0x843C # 3 F
#	FRAGMENT_LIGHT_SPACE_SGIX			= 0x843D # 1 I
#	TANGENT_ARRAY_TYPE_SGIX				= 0x843E
#	TANGENT_ARRAY_STRIDE_SGIX			= 0x843F
#	TANGENT_ARRAY_COUNT_SGIX			= 0x8440
#	BINORMAL_ARRAY_TYPE_SGIX			= 0x8441
#	BINORMAL_ARRAY_STRIDE_SGIX			= 0x8442
#	BINORMAL_ARRAY_COUNT_SGIX			= 0x8443
#	TANGENT_ARRAY_POINTER_SGIX			= 0x8444
#	BINORMAL_ARRAY_POINTER_SGIX			= 0x8445
#	MAP1_TANGENT_SGIX				= 0x8446
#	MAP2_TANGENT_SGIX				= 0x8447
#	MAP1_BINORMAL_SGIX				= 0x8448
#	MAP2_BINORMAL_SGIX				= 0x8449

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_bali_timer_instruments: 0x844A-0x844C
#	BALI_GEOM_TIMER_INSTRUMENT_SGIX			= 0x844A # 1 I
#	BALI_RASTER_TIMER_INSTRUMENT_SGIX		= 0x844B # 1 I
#	BALI_INSTRUMENT_TIME_UNIT_SGIX			= 0x844C # 1 I

###############################################################################

# SGIX_clipmap (additional; see above): 0x844D-0x844F

###############################################################################

# SGI (actually brokered for Id Software): 0x8450-0x845F

# EXT_fog_coord enum:
#	FOG_COORDINATE_SOURCE_EXT			= 0x8450 # 1 I
#	FOG_COORDINATE_EXT				= 0x8451
#	FRAGMENT_DEPTH_EXT				= 0x8452
#	CURRENT_FOG_COORDINATE_EXT			= 0x8453 # 1 F
#	FOG_COORDINATE_ARRAY_TYPE_EXT			= 0x8454 # 1 I
#	FOG_COORDINATE_ARRAY_STRIDE_EXT			= 0x8455 # 1 I
#	FOG_COORDINATE_ARRAY_POINTER_EXT		= 0x8456
#	FOG_COORDINATE_ARRAY_EXT			= 0x8457 # 1 I

# EXT_secondary_color enum:
#	COLOR_SUM_EXT					= 0x8458 # 1 I
#	CURRENT_SECONDARY_COLOR_EXT			= 0x8459 # 3 F
#	SECONDARY_COLOR_ARRAY_SIZE_EXT			= 0x845A # 1 I
#	SECONDARY_COLOR_ARRAY_TYPE_EXT			= 0x845B # 1 I
#	SECONDARY_COLOR_ARRAY_STRIDE_EXT		= 0x845C # 1 I
#	SECONDARY_COLOR_ARRAY_POINTER_EXT		= 0x845D
#	SECONDARY_COLOR_ARRAY_EXT			= 0x845E # 1 I

# SGI_future_use (actually Id Software, see above): 0x845F

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_icc_texture enum:
#	RGB_ICC_SGIX					= 0x8460
#	RGBA_ICC_SGIX					= 0x8461
#	ALPHA_ICC_SGIX					= 0x8462
#	LUMINANCE_ICC_SGIX				= 0x8463
#	INTENSITY_ICC_SGIX				= 0x8464
#	LUMINANCE_ALPHA_ICC_SGIX			= 0x8465
#	R5_G6_B5_ICC_SGIX				= 0x8466
#	R5_G6_B5_A8_ICC_SGIX				= 0x8467
#	ALPHA16_ICC_SGIX				= 0x8468
#	LUMINANCE16_ICC_SGIX				= 0x8469
#	INTENSITY16_ICC_SGIX				= 0x846A
#	LUMINANCE16_ALPHA8_ICC_SGIX			= 0x846B

###############################################################################

# SGI_future_use: 0x846C

###############################################################################

# SMOOTH_* enums are new names for pre-1.2 enums.
VERSION_1_2 enum:
	SMOOTH_POINT_SIZE_RANGE				= 0x0B12 # 2 F
	SMOOTH_POINT_SIZE_GRANULARITY			= 0x0B13 # 1 F
	SMOOTH_LINE_WIDTH_RANGE				= 0x0B22 # 2 F
	SMOOTH_LINE_WIDTH_GRANULARITY			= 0x0B23 # 1 F
	ALIASED_POINT_SIZE_RANGE			= 0x846D # 2 F
	ALIASED_LINE_WIDTH_RANGE			= 0x846E # 2 F

###############################################################################

# SGI_future_use: 0x846F

###############################################################################

# ATI Technologies (vendor multitexture, spec not yet released): 0x8470-0x848F

###############################################################################

# REND (Rendition): 0x8490-0x849F

# REND_screen_coordinates enum:
#	SCREEN_COORDINATES_REND				= 0x8490
#	INVERTED_SCREEN_W_REND				= 0x8491

###############################################################################

# ATI Technologies (vendor multitexture, spec not yet released): 0x84A0-84BF

###############################################################################

#ARB_multitexture enum:
#	TEXTURE0_ARB					= 0x84C0
#	TEXTURE1_ARB					= 0x84C1
#	TEXTURE2_ARB					= 0x84C2
#	TEXTURE3_ARB					= 0x84C3
#	TEXTURE4_ARB					= 0x84C4
#	TEXTURE5_ARB					= 0x84C5
#	TEXTURE6_ARB					= 0x84C6
#	TEXTURE7_ARB					= 0x84C7
#	TEXTURE8_ARB					= 0x84C8
#	TEXTURE9_ARB					= 0x84C9
#	TEXTURE10_ARB					= 0x84CA
#	TEXTURE11_ARB					= 0x84CB
#	TEXTURE12_ARB					= 0x84CC
#	TEXTURE13_ARB					= 0x84CD
#	TEXTURE14_ARB					= 0x84CE
#	TEXTURE15_ARB					= 0x84CF
#	TEXTURE16_ARB					= 0x84D0
#	TEXTURE17_ARB					= 0x84D1
#	TEXTURE18_ARB					= 0x84D2
#	TEXTURE19_ARB					= 0x84D3
#	TEXTURE20_ARB					= 0x84D4
#	TEXTURE21_ARB					= 0x84D5
#	TEXTURE22_ARB					= 0x84D6
#	TEXTURE23_ARB					= 0x84D7
#	TEXTURE24_ARB					= 0x84D8
#	TEXTURE25_ARB					= 0x84D9
#	TEXTURE26_ARB					= 0x84DA
#	TEXTURE27_ARB					= 0x84DB
#	TEXTURE28_ARB					= 0x84DC
#	TEXTURE29_ARB					= 0x84DD
#	TEXTURE30_ARB					= 0x84DE
#	TEXTURE31_ARB					= 0x84DF
#	ACTIVE_TEXTURE_ARB				= 0x84E0 # 1 I
#	CLIENT_ACTIVE_TEXTURE_ARB			= 0x84E1 # 1 I
#	MAX_TEXTURE_UNITS_ARB				= 0x84E2 # 1 I

###############################################################################

# ARB_transpose_matrix enum:
#	TRANSPOSE_MODELVIEW_MATRIX_ARB			= 0x84E3 # 16 F
#	TRANSPOSE_PROJECTION_MATRIX_ARB			= 0x84E4 # 16 F
#	TRANSPOSE_TEXTURE_MATRIX_ARB			= 0x84E5 # 16 F
#	TRANSPOSE_COLOR_MATRIX_ARB			= 0x84E6 # 16 F

# ARB_future_use: 0x84E7-0x84E8
# (previously used in a draft version of ARB_multisample, but not in the
# final ARB-approved version):

# ARB_texture_compression enum:
#	COMPRESSED_ALPHA_ARB				= 0x84E9
#	COMPRESSED_LUMINANCE_ARB			= 0x84EA
#	COMPRESSED_LUMINANCE_ALPHA_ARB			= 0x84EB
#	COMPRESSED_INTENSITY_ARB			= 0x84EC
#	COMPRESSED_RGB_ARB				= 0x84ED
#	COMPRESSED_RGBA_ARB				= 0x84EE
#	TEXTURE_COMPRESSION_HINT_ARB			= 0x84EF
#	TEXTURE_IMAGE_SIZE_ARB				= 0x86A0
#	TEXTURE_COMPRESSED_ARB				= 0x86A1
#	NUM_COMPRESSED_TEXTURE_FORMATS_ARB		= 0x86A2
#	COMPRESSED_TEXTURE_FORMATS_ARB			= 0x86A3

###############################################################################

# Nvidia: 0x84F0-0x855F
# NV_future_use: 0x84F0-0x84FC

# EXT_texture_lod_bias enum:
#	MAX_TEXTURE_LOD_BIAS_EXT			= 0x84FD

# EXT_texture_filter_anisotropic enum:
#	TEXTURE_MAX_ANISOTROPY_EXT			= 0x84FE
#	MAX_TEXTURE_MAX_ANISOTROPY_EXT			= 0x84FF

# EXT_texture_lod_bias enum:
#	TEXTURE_FILTER_CONTROL_EXT			= 0x8500
#	TEXTURE_LOD_BIAS_EXT				= 0x8501

# EXT_vertex_weighting enum:
#	MODELVIEW1_STACK_DEPTH_EXT			= 0x8502
#	<unused>					= 0x8503

# NV_light_max_exponent enum:
#	MAX_SHININESS_NV				= 0x8504
#	MAX_SPOT_EXPONENT_NV				= 0x8505

# EXT_vertex_weighting enum:
#	MODELVIEW_MATRIX1_EXT				= 0x8506

# EXT_stencil_wrap enum:
#	INCR_WRAP_EXT					= 0x8507
#	DECR_WRAP_EXT					= 0x8508

# EXT_vertex_weighting enum:
#	VERTEX_WEIGHTING_EXT				= 0x8509
#	MODELVIEW1_EXT					= 0x850A
#	CURRENT_VERTEX_WEIGHT_EXT			= 0x850B
#	VERTEX_WEIGHT_ARRAY_EXT				= 0x850C
#	VERTEX_WEIGHT_ARRAY_SIZE_EXT			= 0x850D
#	VERTEX_WEIGHT_ARRAY_TYPE_EXT			= 0x850E
#	VERTEX_WEIGHT_ARRAY_STRIDE_EXT			= 0x850F
#	VERTEX_WEIGHT_ARRAY_POINTER_EXT			= 0x8510

# Note: these are also exposed as NV and EXT, as well as ARB
#   NV_texgen_reflection enum:
#   EXT_texture_cube_map enum:
# ARB_texture_cube_map enum:
#	NORMAL_MAP_ARB					= 0x8511
#	REFLECTION_MAP_ARB				= 0x8512
#	TEXTURE_CUBE_MAP_ARB				= 0x8513
#	TEXTURE_BINDING_CUBE_MAP_ARB			= 0x8514
#	TEXTURE_CUBE_MAP_POSITIVE_X_ARB			= 0x8515
#	TEXTURE_CUBE_MAP_NEGATIVE_X_ARB			= 0x8516
#	TEXTURE_CUBE_MAP_POSITIVE_Y_ARB			= 0x8517
#	TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB			= 0x8518
#	TEXTURE_CUBE_MAP_POSITIVE_Z_ARB			= 0x8519
#	TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB			= 0x851A
#	PROXY_TEXTURE_CUBE_MAP_ARB			= 0x851B
#	MAX_CUBE_MAP_TEXTURE_SIZE_ARB			= 0x851C

# NV_vertex_array_range enum:
#	VERTEX_ARRAY_RANGE_NV				= 0x851D
#	VERTEX_ARRAY_RANGE_LENGTH_NV			= 0x851E
#	VERTEX_ARRAY_RANGE_VALID_NV			= 0x851F
#	MAX_VERTEX_ARRAY_RANGE_ELEMENT_NV		= 0x8520
#	VERTEX_ARRAY_RANGE_POINTER_NV			= 0x8521

# NV_register_combiners enum:
#	REGISTER_COMBINERS_NV				= 0x8522
#	VARIABLE_A_NV					= 0x8523
#	VARIABLE_B_NV					= 0x8524
#	VARIABLE_C_NV					= 0x8525
#	VARIABLE_D_NV					= 0x8526
#	VARIABLE_E_NV					= 0x8527
#	VARIABLE_F_NV					= 0x8528
#	VARIABLE_G_NV					= 0x8529
#	CONSTANT_COLOR0_NV				= 0x852A
#	CONSTANT_COLOR1_NV				= 0x852B
#	PRIMARY_COLOR_NV				= 0x852C
#	SECONDARY_COLOR_NV				= 0x852D
#	SPARE0_NV					= 0x852E
#	SPARE1_NV					= 0x852F
#	DISCARD_NV					= 0x8530
#	E_TIMES_F_NV					= 0x8531
#	SPARE0_PLUS_SECONDARY_COLOR_NV			= 0x8532
#	<unused>					= 0x8533
#	<unused>					= 0x8534
#	<unused>					= 0x8535
#	UNSIGNED_IDENTITY_NV				= 0x8536
#	UNSIGNED_INVERT_NV				= 0x8537
#	EXPAND_NORMAL_NV				= 0x8538
#	EXPAND_NEGATE_NV				= 0x8539
#	HALF_BIAS_NORMAL_NV				= 0x853A
#	HALF_BIAS_NEGATE_NV				= 0x853B
#	SIGNED_IDENTITY_NV				= 0x853C
#	UNSIGNED_NEGATE_NV				= 0x853D
#	SCALE_BY_TWO_NV					= 0x853E
#	SCALE_BY_FOUR_NV				= 0x853F
#	SCALE_BY_ONE_HALF_NV				= 0x8540
#	BIAS_BY_NEGATIVE_ONE_HALF_NV			= 0x8541
#	COMBINER_INPUT_NV				= 0x8542
#	COMBINER_MAPPING_NV				= 0x8543
#	COMBINER_COMPONENT_USAGE_NV			= 0x8544
#	COMBINER_AB_DOT_PRODUCT_NV			= 0x8545
#	COMBINER_CD_DOT_PRODUCT_NV			= 0x8546
#	COMBINER_MUX_SUM_NV				= 0x8547
#	COMBINER_SCALE_NV				= 0x8548
#	COMBINER_BIAS_NV				= 0x8549
#	COMBINER_AB_OUTPUT_NV				= 0x854A
#	COMBINER_CD_OUTPUT_NV				= 0x854B
#	COMBINER_SUM_OUTPUT_NV				= 0x854C
#	MAX_GENERAL_COMBINERS_NV			= 0x854D
#	NUM_GENERAL_COMBINERS_NV			= 0x854E
#	COLOR_SUM_CLAMP_NV				= 0x854F
#	COMBINER0_NV					= 0x8550
#	COMBINER1_NV					= 0x8551
#	COMBINER2_NV					= 0x8552
#	COMBINER3_NV					= 0x8553
#	COMBINER4_NV					= 0x8554
#	COMBINER5_NV					= 0x8555
#	COMBINER6_NV					= 0x8556
#	COMBINER7_NV					= 0x8557
#	<unused>					= 0x8558
#	<unused>					= 0x8559

# NV_fog_distance enum:
#	FOG_GEN_MODE_NV					= 0x855A
#	EYE_RADIAL_NV					= 0x855B
#	EYE_PLANE_ABSOLUTE_NV				= 0x855C

# NV_texgen_emboss enum:
#	EMBOSS_LIGHT_NV					= 0x855D
#	EMBOSS_CONSTANT_NV				= 0x855E
#	EMBOSS_MAP_NV					= 0x855F

###############################################################################

# Intergraph: 0x8560-0x856F

# INGR_color_clamp enum:
#	RED_MIN_CLAMP_INGR				= 0x8560
#	GREEN_MIN_CLAMP_INGR				= 0x8561
#	BLUE_MIN_CLAMP_INGR				= 0x8562
#	ALPHA_MIN_CLAMP_INGR				= 0x8563
#	RED_MAX_CLAMP_INGR				= 0x8564
#	GREEN_MAX_CLAMP_INGR				= 0x8565
#	BLUE_MAX_CLAMP_INGR				= 0x8566
#	ALPHA_MAX_CLAMP_INGR				= 0x8567

# INGR_interlace_read enum:
#	INTERLACE_READ_INGR				= 0x8568

###############################################################################

# ATI/Nvidia: 0x8570-0x859F

# EXT_texture_env_combine enum:
#	COMBINE_EXT					= 0x8570
#	COMBINE_RGB_EXT					= 0x8571
#	COMBINE_ALPHA_EXT				= 0x8572
#	RGB_SCALE_EXT					= 0x8573
#	ADD_SIGNED_EXT					= 0x8574
#	INTERPOLATE_EXT					= 0x8575
#	CONSTANT_EXT					= 0x8576
#	PRIMARY_COLOR_EXT				= 0x8577
#	PREVIOUS_EXT					= 0x8578
#	SOURCE0_RGB_EXT					= 0x8580
#	SOURCE1_RGB_EXT					= 0x8581
#	SOURCE2_RGB_EXT					= 0x8582
#	SOURCE3_RGB_EXT					= 0x8583
#	SOURCE4_RGB_EXT					= 0x8584
#	SOURCE5_RGB_EXT					= 0x8585
#	SOURCE6_RGB_EXT					= 0x8586
#	SOURCE7_RGB_EXT					= 0x8587
#	SOURCE0_ALPHA_EXT				= 0x8588
#	SOURCE1_ALPHA_EXT				= 0x8589
#	SOURCE2_ALPHA_EXT				= 0x858A
#	SOURCE3_ALPHA_EXT				= 0x858B
#	SOURCE4_ALPHA_EXT				= 0x858C
#	SOURCE5_ALPHA_EXT				= 0x858D
#	SOURCE6_ALPHA_EXT				= 0x858E
#	SOURCE7_ALPHA_EXT				= 0x858F
#	OPERAND0_RGB_EXT				= 0x8590
#	OPERAND1_RGB_EXT				= 0x8591
#	OPERAND2_RGB_EXT				= 0x8592
#	OPERAND3_RGB_EXT				= 0x8593
#	OPERAND4_RGB_EXT				= 0x8594
#	OPERAND5_RGB_EXT				= 0x8595
#	OPERAND6_RGB_EXT				= 0x8596
#	OPERAND7_RGB_EXT				= 0x8597
#	OPERAND0_ALPHA_EXT				= 0x8598
#	OPERAND1_ALPHA_EXT				= 0x8599
#	OPERAND2_ALPHA_EXT				= 0x859A
#	OPERAND3_ALPHA_EXT				= 0x859B
#	OPERAND4_ALPHA_EXT				= 0x859C
#	OPERAND5_ALPHA_EXT				= 0x859D
#	OPERAND6_ALPHA_EXT				= 0x859E
#	OPERAND7_ALPHA_EXT				= 0x859F

###############################################################################

SGIX_subsample enum:
	PACK_SUBSAMPLE_RATE_SGIX			= 0x85A0
	UNPACK_SUBSAMPLE_RATE_SGIX			= 0x85A1
	PIXEL_SUBSAMPLE_4444_SGIX			= 0x85A2
	PIXEL_SUBSAMPLE_2424_SGIX			= 0x85A3
	PIXEL_SUBSAMPLE_4242_SGIX			= 0x85A4

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIS_color_range: 0x85A5-0x85AD
#	EXTENDED_RANGE_SGIS				= 0x85A5
#	MIN_RED_SGIS					= 0x85A6
#	MAX_RED_SGIS					= 0x85A7
#	MIN_GREEN_SGIS					= 0x85A8
#	MAX_GREEN_SGIS					= 0x85A9
#	MIN_BLUE_SGIS					= 0x85AA
#	MAX_BLUE_SGIS					= 0x85AB
#	MIN_ALPHA_SGIS					= 0x85AC
#	MAX_ALPHA_SGIS					= 0x85AD

###############################################################################

# EXT_texture_perturb_normal enum:
#	PERTURB_EXT					= 0x85AE
#	TEXTURE_NORMAL_EXT				= 0x85AF

###############################################################################

# Apple: 0x85B0-0x85BF

#	LIGHT_MODEL_SPECULAR_VECTOR_APPLE		= 0x85B0
#	TRANSFORM_HINT_APPLE				= 0x85B1

###############################################################################

# Sun: 0x85C0-0x85CF

# SUNX_general_triangle_list (additional; see above): 0x85C0-0x85CB

###############################################################################

# Unknown extension name, not in enumext.spec
# 3Dlabs/Autodesk: 0x85D0-0x85DF
#	FACET_NORMAL_AUTODESK				= 0x85D0
#	FACET_NORMAL_ARRAY_AUTODESK			= 0x85D1

###############################################################################

# Incomplete extension, not in enumext.spec
# SGIX_texture_range: 0x85E0-0x85FB
#	RGB_SIGNED_SGIX					= 0x85E0
#	RGBA_SIGNED_SGIX				= 0x85E1
#	ALPHA_SIGNED_SGIX				= 0x85E2
#	LUMINANCE_SIGNED_SGIX				= 0x85E3
#	INTENSITY_SIGNED_SGIX				= 0x85E4
#	LUMINANCE_ALPHA_SIGNED_SGIX			= 0x85E5
#	RGB16_SIGNED_SGIX				= 0x85E6
#	RGBA16_SIGNED_SGIX				= 0x85E7
#	ALPHA16_SIGNED_SGIX				= 0x85E8
#	LUMINANCE16_SIGNED_SGIX				= 0x85E9
#	INTENSITY16_SIGNED_SGIX				= 0x85EA
#	LUMINANCE16_ALPHA16_SIGNED_SGIX			= 0x85EB
#	RGB_EXTENDED_RANGE_SGIX				= 0x85EC
#	RGBA_EXTENDED_RANGE_SGIX			= 0x85ED
#	ALPHA_EXTENDED_RANGE_SGIX			= 0x85EE
#	LUMINANCE_EXTENDED_RANGE_SGIX			= 0x85EF
#	INTENSITY_EXTENDED_RANGE_SGIX			= 0x85F0
#	LUMINANCE_ALPHA_EXTENDED_RANGE_SGIX		= 0x85F1
#	RGB16_EXTENDED_RANGE_SGIX			= 0x85F2
#	RGBA16_EXTENDED_RANGE_SGIX			= 0x85F3
#	ALPHA16_EXTENDED_RANGE_SGIX			= 0x85F4
#	LUMINANCE16_EXTENDED_RANGE_SGIX			= 0x85F5
#	INTENSITY16_EXTENDED_RANGE_SGIX			= 0x85F6
#	LUMINANCE16_ALPHA16_EXTENDED_RANGE_SGIX		= 0x85F7
#	MIN_LUMINANCE_SGIS				= 0x85F8
#	MAX_LUMINANCE_SGIS				= 0x85F9
#	MIN_INTENSITY_SGIS				= 0x85FA
#	MAX_INTENSITY_SGIS				= 0x85FB

###############################################################################

# SGI_future_use: 0x85FC-0x85FF

###############################################################################

# Sun: 0x8600-0x861F

###############################################################################

# NVIDIA: 0x8620-0x867F

###############################################################################

# Pixelfusion: 0x8680-0x869F

###############################################################################

# ARB: 0x86A0-0x86AF

# ARB_texture_compression (additional; see above): 0x86A0-0x86A3

# ARB_future_use: 0x86A4-0x86AF

###############################################################################

# 3Dfx: 0x86B0-0x86BF

# 3DFX_texture_compression_FXT1 enum:
#	COMPRESSED_RGB_FXT1_3DFX			= 0x86B0
#	COMPRESSED_RGBA_FXT1_3DFX			= 0x86B1

# 3DFX_multisample enum:
#	MULTISAMPLE_3DFX				= 0x86B2
#	SAMPLE_BUFFERS_3DFX				= 0x86B3
#	SAMPLES_3DFX					= 0x86B4
#	MULTISAMPLE_BIT_3DFX				= 0x20000000

###############################################################################

###############################################################################
### PLEASE REMEMBER THAT NEW ENUMERANT ALLOCATIONS MUST BE OBTAINED BY
### REQUEST TO SGI'S ARB REPRESENTATIVE (see comments at the top of this file)
###############################################################################

# Any_vendor_future_use: 0x86C0-0xFFFF
#
#   This range must be the last range in the file.  To generate a new
#   range, allocate multiples of 16 from the beginning of the
#   Any_vendor_future_use range and update enum.spec

###############################################################################

# ARB:	  100000-100999 (GLU enumerants only)
# ARB:	  101000-101999 (Conformance tests only)

###############################################################################

# IBM:	  103000-103999
#	CULL_VERTEX_IBM					= 103050
#	VERTEX_ARRAY_LIST_IBM				= 103070
#	NORMAL_ARRAY_LIST_IBM				= 103071
#	COLOR_ARRAY_LIST_IBM				= 103072
#	INDEX_ARRAY_LIST_IBM				= 103073
#	TEXTURE_COORD_ARRAY_LIST_IBM			= 103074
#	EDGE_FLAG_ARRAY_LIST_IBM			= 103075
#	FOG_COORDINATE_ARRAY_LIST_IBM			= 103076
#	SECONDARY_COLOR_ARRAY_LIST_IBM			= 103077
#	VERTEX_ARRAY_LIST_STRIDE_IBM			= 103080
#	NORMAL_ARRAY_LIST_STRIDE_IBM			= 103081
#	COLOR_ARRAY_LIST_STRIDE_IBM			= 103082
#	INDEX_ARRAY_LIST_STRIDE_IBM			= 103083
#	TEXTURE_COORD_ARRAY_LIST_STRIDE_IBM		= 103084
#	EDGE_FLAG_ARRAY_LIST_STRIDE_IBM			= 103085
#	FOG_COORDINATE_ARRAY_LIST_STRIDE_IBM		= 103086
#	SECONDARY_COLOR_ARRAY_LIST_STRIDE_IBM		= 103087

###############################################################################

# NEC:	  104000-104999
# Compaq: 105000-105999
# KPC:	  106000-106999 (Kubota is out of business)
# PGI:	  107000-107999 (Portable was acquired by Template Graphics)
# E&S:	  108000-108999

###############################################################################
