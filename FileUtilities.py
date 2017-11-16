from Body import *
from PyQt4.QtGui import *

class FileUtilities:
    def exportBodiesFile(name):
        global gBodies
        export_file = open(name, 'w')
        # Limpiando el file
        export_file.seek(0)
        export_file.truncate()

        # Exportando todos los cuerpos presente en gBodies
        for b in gBodies:
            line_string = "{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|\n".format(b.id,b.mass, b.r[0], b.r[1], b.r[2], b.v[0], b.v[1], b.v[2], b.color, int(b.light))
            export_file.write(line_string)
        export_file.close()

    def importBodiesFile(name, combo):
        global gBodies
        buffer = []
        import_file = open(name, 'r')
        for line in import_file:
            current_data = ""
            data_list = list()
            for ch in line:
                # Caracteres de separacion
                if ch != '|' and ch != ',':
                    if ch != " " and ch != '(' and ch != ')': # Ignorando los espacios
                        current_data += str(ch)
                else:
                    data_list.append(current_data)
                    current_data = ""
            # Acabada de leer una linea, se carga el objeto con sus datos
            temp_body = Body(data_list[0],
                                float(data_list[1]),
                                float(data_list[2]),float(data_list[3]),float(data_list[4]),
                                float(data_list[5]),float(data_list[6]),float(data_list[7]),
                                (float(data_list[8]),float(data_list[9]),float(data_list[10])),
                                bool(int(data_list[11])))

            buffer.append(temp_body)
        # Acabado el anexo de los cuerpos, se actualiza el combo
        gBodies[:] = buffer[:]
        FileUtilities.refreshBodiesCombo(combo)
        import_file.close()

    def refreshBodiesCombo(combo):
        combo.clear()
        global gBodies
        for b in gBodies:
            combo.addItem(b.id)
