import React, { useState } from 'react';
import {
  Text,
  View,
  Button,
  StyleSheet,
  Modal,
  ScrollView,
  TouchableOpacity,
  TextInput,
  Alert
} from 'react-native';

export default function App() {
  // Lista inicial de receitas
  const [listaReceitas, setListaReceitas] = useState([
    {
      id: '1',
      nome: 'Bolo de Cenoura com Cobertura de Chocolate',
      ingredientes: `3 cenouras médias picadas\n3 ovos\n1 xícara de óleo\n2 xícaras de açúcar\n2 xícaras de farinha de trigo\n1 colher (sopa) de fermento em pó`,
      modoPreparo: `1. Bata no liquidificador a cenoura, ovos e óleo.\n2. Misture o açúcar e a farinha em uma tigela.\n3. Junte as misturas, adicione o fermento e mexe delicadamente.\n4. Asse em forno pré-aquecido a 180°C por 40 minutos.`
    }
  ]);

  // Estados dos Modais
  const [modalVerVisivel, setModalVerVisivel] = useState(false);
  const [modalCadastroVisivel, setModalCadastroVisivel] = useState(false);

  // Receita selecionada para ser exibida no Modal "Ver Receita"
  const [receitaSelecionada, setReceitaSelecionada] = useState(null);

  // Estados dos campos de cadastro de receita
  const [nome, setNome] = useState('');
  const [ingredientes, setIngredientes] = useState('');
  const [modoPreparo, setModoPreparo] = useState('');

  // Função para abrir o modal de visualização de uma receita específica
  const abrirVisualizacao = (receita) => {
    setReceitaSelecionada(receita);
    setModalVerVisivel(true);
  };

  // Função para salvar uma nova receita
  const salvarReceita = () => {
    if (!nome.trim() || !ingredientes.trim() || !modoPreparo.trim()) {
      Alert.alert('Atenção', 'Por favor, preencha todos os campos!');
      return;
    }

    const novaReceita = {
      id: Date.now().toString(),
      nome,
      ingredientes,
      modoPreparo
    };

    setListaReceitas((receitasAnteriores) => [...receitasAnteriores, novaReceita]);
    
    Alert.alert('Sucesso', 'Receita cadastrada com sucesso!');
    limparFormularioECFechar();
  };

  // Função para cancelar o cadastro
  const cancelarCadastro = () => {
    limparFormularioECFechar();
  };

  // Limpa os campos do formulário e fecha o modal de cadastro
  const limparFormularioECFechar = () => {
    setNome('');
    setIngredientes('');
    setModoPreparo('');
    setModalCadastroVisivel(false);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>📱 App de Receitas</Text>
      <Text style={styles.subtitle}>Colecione suas receitas preferidas</Text>

      {/* Lista de Receitas em ScrollView */}
      <ScrollView 
        style={styles.scrollContainer}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        {listaReceitas.map((receita) => (
          <View key={receita.id} style={styles.card}>
            <Text style={styles.cardTitle}>{receita.nome}</Text>
            <Button title="Ver Receita" onPress={() => abrirVisualizacao(receita)} />
          </View>
        ))}
      </ScrollView>

      {/* MODAL 1: Ver Receita */}
      <Modal
        animationType="slide"
        transparent={true}
        visible={modalVerVisivel}
        onRequestClose={() => setModalVerVisivel(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContainer}>
            {receitaSelecionada && (
              <ScrollView showsVerticalScrollIndicator={false}>
                <Text style={styles.recipeTitle}>{receitaSelecionada.nome}</Text>

                <Text style={styles.sectionHeader}>🛒 Ingredientes</Text>
                <Text style={styles.recipeText}>{receitaSelecionada.ingredientes}</Text>

                <Text style={styles.sectionHeader}>👨‍🍳 Modo de Preparo</Text>
                <Text style={styles.recipeText}>{receitaSelecionada.modoPreparo}</Text>
              </ScrollView>
            )}

            <View style={styles.modalButtonContainer}>
              <Button title="Fechar" onPress={() => setModalVerVisivel(false)} color="#D9534F" />
            </View>
          </View>
        </View>
      </Modal>

      {/* MODAL 2: Cadastro de Receita */}
      <Modal
        animationType="slide"
        transparent={true}
        visible={modalCadastroVisivel}
        onRequestClose={cancelarCadastro}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContainer}>
            <Text style={styles.modalHeaderTitle}>Nova Receita</Text>

            <ScrollView showsVerticalScrollIndicator={false}>
              <Text style={styles.label}>Nome da Receita:</Text>
              <TextInput
                style={styles.input}
                placeholder="Ex: Bolo de Cenoura"
                value={nome}
                onChangeText={setNome}
              />

              <Text style={styles.label}>Ingredientes:</Text>
              <TextInput
                style={[styles.input, styles.textArea]}
                placeholder="Ex: 3 cenouras, 3 ovos, 2 xícaras de açúcar..."
                value={ingredientes}
                onChangeText={setIngredientes}
                multiline={true}
                numberOfLines={4}
                textAlignVertical="top"
              />

              <Text style={styles.label}>Modo de Preparo:</Text>
              <TextInput
                style={[styles.input, styles.textArea]}
                placeholder="Ex: 1. Bata a cenoura e os ovos no liquidificador..."
                value={modoPreparo}
                onChangeText={setModoPreparo}
                multiline={true}
                numberOfLines={4}
                textAlignVertical="top"
              />
            </ScrollView>

            <View style={styles.formButtonRow}>
              <View style={styles.buttonWrapper}>
                <Button title="Cancelar" onPress={cancelarCadastro} color="#D9534F" />
              </View>
              <View style={styles.buttonWrapper}>
                <Button title="Salvar" onPress={salvarReceita} color="#28A745" />
              </View>
            </View>
          </View>
        </View>
      </Modal>

      {/* Botão Flutuante (FAB) */}
      <TouchableOpacity
        style={styles.fab}
        onPress={() => setModalCadastroVisivel(true)}
        activeOpacity={0.8}
      >
        <Text style={styles.fabText}>+</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 50,
    backgroundColor: '#BAB5B5',
    alignItems: 'center',
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 5,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 20,
    marginBottom: 15,
    textAlign: 'center',
  },

  // ScrollView & Cartões na Tela Inicial
  scrollContainer: {
    width: '100%',
  },
  scrollContent: {
    paddingHorizontal: 20,
    paddingBottom: 90, // Espaço extra para não cobrir o último card com o FAB
  },
  card: {
    backgroundColor: '#FFF',
    padding: 18,
    borderRadius: 12,
    marginBottom: 15,
    elevation: 3,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 3,
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 12,
  },

  // Estilos de Modais Generais
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  modalContainer: {
    width: '100%',
    maxHeight: '85%',
    backgroundColor: '#FFF',
    borderRadius: 15,
    padding: 20,
    elevation: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 4,
  },

  // Modal Ver Receita
  recipeTitle: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
    textAlign: 'center',
  },
  sectionHeader: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#007AFF',
    marginTop: 15,
    marginBottom: 8,
  },
  recipeText: {
    fontSize: 15,
    color: '#444',
    lineHeight: 22,
    whiteSpace: 'pre-line', // Preserva as quebras de linha digitadas
  },
  modalButtonContainer: {
    marginTop: 15,
  },

  // Modal Cadastro
  modalHeaderTitle: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 15,
    textAlign: 'center',
  },
  label: {
    fontSize: 15,
    fontWeight: 'bold',
    color: '#444',
    marginTop: 10,
    marginBottom: 5,
  },
  input: {
    backgroundColor: '#F5F5F5',
    borderWidth: 1,
    borderColor: '#DDD',
    borderRadius: 8,
    padding: 10,
    fontSize: 15,
  },
  textArea: {
    minHeight: 80,
  },
  formButtonRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 20,
  },
  buttonWrapper: {
    flex: 0.48,
  },

  // Estilos do FAB (Botão Flutuante)
  fab: {
    position: 'absolute',
    bottom: 24,
    right: 24,
    width: 60,
    height: 60,
    borderRadius: 30,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#007AFF',
    elevation: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 3,
  },
  fabText: {
    fontSize: 28,
    color: '#fff',
    fontWeight: 'bold',
  },
});