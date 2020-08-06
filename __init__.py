# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Manejo
                                 A QGIS plugin
 Manejo plugin
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-07-25
        copyright            : (C) 2020 by Carvalho Neto, R.M./ Sustembio Environmental Services
        email                : romariocarvalho@hotmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Manejo class from file Manejo.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .manejo import Manejo
    return Manejo(iface)